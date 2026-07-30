from controller import Supervisor
import math

supervisor = Supervisor()
time_step = 64

robot_node = supervisor.getFromDef("robot")
if robot_node is None:
    print("Error: No robot with DEF 'robot' found.")
    exit()

left_motor = supervisor.getDevice("left wheel motor")
right_motor = supervisor.getDevice("right wheel motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

gps = supervisor.getDevice("gps")
if gps is not None:
    gps.enable(time_step)
else:
    print("Warning: GPS not found, using node position.")

center_x, center_y = 0, 0
radius = 2.0
angle = 0.0
angular_speed = 0.05

while supervisor.step(time_step) != -1:
    target_x = center_x + radius * math.cos(angle)
    target_y = center_y + radius * math.sin(angle)

    if gps is not None:
        pos = gps.getValues()
        current_x, current_y = pos[0], pos[1]
    else:
        pos = robot_node.getPosition()
        current_x, current_y = pos[0], pos[1]

    dx = target_x - current_x
    dy = target_y - current_y
    distance = math.hypot(dx, dy)

    if distance < 0.1:
        angle += angular_speed
        left_motor.setVelocity(2.0)
        right_motor.setVelocity(2.0)
        continue

    target_heading = math.atan2(dy, dx)
    orientation = robot_node.getOrientation()
    heading = math.atan2(orientation[3], orientation[0])

    diff = target_heading - heading
    while diff > math.pi:
        diff -= 2 * math.pi
    while diff < -math.pi:
        diff += 2 * math.pi

    turn_speed = max(-3.0, min(3.0, diff * 5.0))
    left_motor.setVelocity(2.0 - turn_speed)
    right_motor.setVelocity(2.0 + turn_speed)