Industrial Object Classifier for Robotic Sorting 🤖
This project implements a Deep Learning solution for classifying industrial components, bridging the gap between Mechatronics hardware and AI.

🛠 Technical Overview
Model: MobileNetV2 (optimized for low-latency inference on edge devices).

Framework: TensorFlow / Keras.

Application: Automated quality control and robotic assembly line sorting.

🎯 Mechatronics Integration
As a Mechatronics Engineer, I designed this script to be compatible with robotic vision systems. The model can be integrated with:

Sensors: Triggering the camera via proximity sensors.

Actuators: Sending classification signals (e.g., via Serial/ROS) to a robotic arm for sorting.

📈 Future Work
Implementing TensorRT for faster inference on NVIDIA Jetson.

Integrating with a PID-controlled conveyor system.
