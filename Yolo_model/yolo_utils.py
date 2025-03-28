import os
from ultralytics import YOLO

def train_model(config_path):
    model = YOLO("yolov8n.yaml")  # Load YOLOv8 nano model
    model.train(data=config_path, epochs=50, imgsz=640, project="runs/train", name="fish_detection")

def evaluate_model(config_path, weights_path):
    model = YOLO(weights_path)  # Load trained model
    metrics = model.val(data=config_path, imgsz=640)
    print("Evaluation Metrics:", metrics)
