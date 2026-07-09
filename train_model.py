from ultralytics import YOLO
import os

def train_yolo():
    # Model load karein (Nano model best hai CPU ke liye)
    model = YOLO("yolo11n.pt")

    # Dataset folder ka path
    dataset_dir = os.path.join(os.getcwd(), "dataset")
    data_yaml = os.path.join(dataset_dir, "data.yaml")

    # Training start karein
    model.train(
        data=data_yaml,
        epochs=50,
        imgsz=640,
        batch=8,
        workers=0  # Windows CPU training ke liye 0 zaroori hai
    )

if __name__ == "__main__":
    train_yolo()