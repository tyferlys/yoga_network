import os
from ultralytics import YOLO


class YogaNetwork:
    def learn(self):
        model = YOLO('yolov8n-cls.pt')
        results = model.train(data="./datasets/yoga82", imgsz=224, epochs=30)

    def predict(self, fileName):
        model = YOLO('./runs/classify/train2/weights/best.pt')
        results = model([f"./images_for_predict/{fileName}"])

        for result in results:
            boxes = result.boxes
            masks = result.masks
            keypoints = result.keypoints
            probs = result.probs
            obb = result.obb

            return str(probs.top1)


