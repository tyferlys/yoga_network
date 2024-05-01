import os
from ultralytics import YOLO


class YogaNetwork:
    @classmethod
    def learn(cls):
        model = YOLO('yolov8n-cls.pt')
        results = model.train(data="./datasets/yoga82", imgsz=224, epochs=30)

    @classmethod
    def predict(cls):
        model = YOLO('./runs/classify/train2/weights/best.pt')
        results = model(["img.png"])

        for result in results:
            boxes = result.boxes
            masks = result.masks
            keypoints = result.keypoints
            probs = result.probs
            obb = result.obb

            print(boxes, masks, keypoints, probs, obb)

            result.show()
            result.save(filename='result.jpg')


YogaNetwork.predict()
