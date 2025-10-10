#!/usr/bin/env python3
import cv2
from ultralytics import YOLO
import pyautogui
import torch

# --- settings you can tweak ---
FRAME_SKIP = 2          # run detection every Nth frame (2 = ~half the work)
IMGSZ = 480             # inference size (320/480/640). Smaller = faster
CONF = 0.4              # confidence threshold
CAM_W, CAM_H, CAM_FPS = 640, 360, 30

# screen setup
screen_width, screen_height = pyautogui.size()

# load model
model = YOLO("yolov8n.pt")
model.fuse()
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# restrict classes (YOLOv8 uses COCO indices)
# person=0, chair=56, cell phone=67, keyboard=66
allowed_classes = [0, 56, 66, 67]

# webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access webcam")
    raise SystemExit

# try to lower camera load (ignored if unsupported)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_H)
cap.set(cv2.CAP_PROP_FPS, CAM_FPS)

window_name = "Live Detection"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, screen_width // 2, screen_height // 2)  # half screen size

frame_i = 0
last_annotated = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # only run detection every Nth frame
    if frame_i % FRAME_SKIP == 0:
        results = model.predict(
            frame,
            imgsz=IMGSZ,
            conf=CONF,
            device=device,
            half=(device != "cpu"),
            classes=allowed_classes,  # restrict classes
            verbose=False
        )
        last_annotated = results[0].plot()

    # reuse last result to keep display smooth
    display = last_annotated if last_annotated is not None else frame
    cv2.imshow(window_name, display)

    frame_i += 1
    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
