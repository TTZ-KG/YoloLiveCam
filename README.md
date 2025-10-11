# Live camera detection with YOLO
This project uses YOLOv8 for real-time object detection, identifying people and various everyday objects using either a connected USB camera or the device’s built-in webcam.

The full list of classes with their identification numbers can be found [here](https://gist.github.com/rcland12/dc48e1963268ff98c8b2c4543e7a9be8#file-yolo_classes-json)


![Live Detection Example](Example.jpg)

## Features
- Real-time object detection  
- Lightweight YOLOv8n model for fast performance  
- Works on CPU or GPU  
- Simple configuration for frame size, confidence threshold, and FPS 

## Prerequisites
- A working webcam (USB or built-in) 
- Python 3.9 or higher  
- pip  
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
[Dalia Mahdy](https://ttz-kg.thws.de/en/about-us/team/?tx_fhwspersonen_fe%5Bperson%5D=5157&tx_fhwspersonen_fe%5Bcontroller%5D=Person&cHash=cdb03945df74ae57cb4e54471e15db7f)

## Acknowledgments
* [YOLO]([https://github.com/matiassingers/awesome-readme](https://docs.ultralytics.com/))
