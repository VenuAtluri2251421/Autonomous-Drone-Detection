# 🚁 Autonomous Drone with Object Detection  

An **autonomous drone framework** built for Raspberry Pi, featuring real-time **YOLO-based object detection** and a modular control system.  
This repository demonstrates how drones can integrate **computer vision** for smart navigation and surveillance tasks.  

---

## 📂 Repository Structure  

```
autonomous-drone/
│── drone_controller.py       # Main controller for drone logic
│── object_detection.py       # Object detection with YOLO
│── utils/
│   └── camera_stream.py      # Camera streaming utility
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
```

---

## ✨ Features  

- 🚀 **Autonomous Flight Simulation** – Takeoff, patrol, and landing logic.  
- 🧠 **Object Detection (YOLO)** – Detects real-world objects like people, cars, animals.  
- 🎥 **Live Camera Stream** – Works with Raspberry Pi Camera Module or USB webcams.  
- 🔗 **Modular Design** – Easy integration with real drone SDKs (DJI Tello, ArduPilot, PX4, etc.).  
- 📡 **Raspberry Pi Ready** – Lightweight and optimized for edge devices.  

---

## 🛠 Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/autonomous-drone.git
   cd autonomous-drone
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Enable Raspberry Pi Camera:  
   ```bash
   sudo raspi-config
   ```

---

## 🚀 Usage  

Run the drone controller:  

```bash
python drone_controller.py
```

The script will:  
- Simulate drone **takeoff**  
- Begin **patrol mode**  
- Perform **object detection**  
- **Hover or land** depending on detections  

---

## 🤖 Object Detection with YOLO  

This project uses **YOLO (You Only Look Once)** for real-time detection.  
To train and export your own YOLO models, refer to my other repository:  

👉 [Learn YOLO in 6 Steps](https://github.com/VenuAtluri2251421/learn-yolo-in-6-steps)  

Once trained, place the exported YOLO weights in:  
```
autonomous-drone/yolo_model/
```

---

## 📸 Example Output  

```
[DRONE] Taking off...
[DRONE] Hovering at safe altitude.
[DRONE] Starting patrol mode...
[DETECTION] Objects detected: ['person']
[DRONE] Person detected! Hovering in place.
[DRONE] Landing...
[DRONE] Drone landed successfully.
```

---

## 📌 Notes  

- This is a **sample framework** for demonstration and prototyping.  
- Replace placeholder functions with real drone SDK calls for full automation.  
- Designed for **Raspberry Pi** but adaptable to other platforms.  

---

## 📚 References  

- [YOLO Object Detection](https://github.com/VenuAtluri2251421/learn-yolo-in-6-steps)  
- [OpenCV Documentation](https://docs.opencv.org/)  
- [Drone SDKs: PX4, ArduPilot, DJI Tello]  

---

## 🌟 Future Improvements  

- Add obstacle avoidance using **LiDAR / depth cameras**.  
- Implement **GPS-based waypoint navigation**.  
- Integrate **LoRa / 5G communication** for long-range missions.  

---

## 👨‍💻 Author  

Built with ❤️ by Venu Atluri (https://github.com/VenuAtluri2251421)
