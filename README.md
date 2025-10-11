# Live camera detection with YOLO

This project uses YOLOv8 for real-time object detection, identifying people and various everyday objects using either a connected USB camera or the device’s built-in webcam.

## Features
- Real-time object detection  
- Lightweight YOLOv8n model for fast performance  
- Works on CPU or GPU  
- Simple configuration for frame size, confidence threshold, and FPS 

## Prerequisites
- Python 3.9 or higher  
- pip  
- A working webcam (USB or built-in)  
- Optionally, a CUDA-capable GPU for faster inference  

### Installing

Install the required packages:
```bash
pip install ultralytics opencv-python pyautogui torch
```
### Executing program

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yolo-live-detection.git
cd yolo-live-detection
```
2. Run the script:
```bash
python detect_live.py
```
## Contact

[Dalia Mahdy]([dalia.mahdy@thws.de](https://ttz-kg.thws.de/en/about-us/team/?tx_fhwspersonen_fe%5Bperson%5D=5157&tx_fhwspersonen_fe%5Bcontroller%5D=Person&cHash=cdb03945df74ae57cb4e54471e15db7f))

## Acknowledgments

Inspiration, code snippets, etc.
* [YOLO]([https://github.com/matiassingers/awesome-readme](https://docs.ultralytics.com/))
