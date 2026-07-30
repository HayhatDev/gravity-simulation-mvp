# 🌌 Gravity Simulation — Circular Path Robot (MVP)

A virtual robot follows a circular path using a **P-Controller** in **Webots** and **Python**.

---

## 🧠 Overview

This project simulates a planet orbiting a star. The robot moves in a smooth, continuous circular path using a simple **proportional controller** (P-Controller). It uses GPS for real-time position tracking and adjusts its wheel speeds to stay on track.

This is the **Minimum Viable Product (MVP)**: a solid foundation for future upgrades like gravity simulation, elliptical orbits, and multiple planets.

---

## ✨ Features

- ✅ Smooth circular motion
- ✅ P-Controller for stable path following
- ✅ GPS-based position tracking
- ✅ Clean and extendable Python code
- ✅ Works with Webots Supervisor API

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Webots** | Simulation environment |
| **Python** | Programming language |
| **Supervisor API** | World control and robot node access |
| **GPS** | Real-time position tracking |

---

## 🎮 How to Run

1. Open `gravity_simulation.wbt` in Webots.
2. Make sure the robot has `DEF = "robot"` and `supervisor = TRUE`.
3. Make sure adding GPS device in the robot "turretSlot".
4. Run the simulation ▶️.
5. The robot will start moving in a circular path.

---

## 🧪 Code Snippet (P-Controller Logic)

```
dx = target_x - current_x
dy = target_y - current_y
target_heading = math.atan2(dy, dx)
heading = math.atan2(orientation[3], orientation[0])
diff = target_heading - heading

turn_speed = max(-3.0, min(3.0, diff * 5.0))
left_motor.setVelocity(2.0 - turn_speed)
right_motor.setVelocity(2.0 + turn_speed)
```
---

## 📂 Project Structure

Gravity-Simulation/

├── worlds/

│   └── Gravity_Simulation.wbt

├── controllers/

│   └── gravity_controller/

│       └── gravity_controller.py

└── README.md

---

## 🎥 Demo Video
[Click Here!](https://youtu.be/yGCKrWO028A)

---

## 🚀 Future Improvements:

🌍 Add gravity simulation (speed varies with distance)

🪐 Convert to elliptical orbits (Kepler's laws)

🌞 Multiple planets (robots) with different orbits

🌟 Interactive control panel (Streamlit)

## 👨‍💻 Author
Hayhat Tahir

📸 Instagram: [@Zanst.21](https://www.instagram.com/zanst.21)


## 📄 License
MIT License: free to use, modify, and distribute with attribution.
