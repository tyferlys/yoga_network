import base64
import json
from datetime import datetime
from io import BytesIO
from PIL import Image
from fastapi import Depends

from YogaNetwork import YogaNetwork
from server.routers.network.schemas.PredictRequest import PredictGetResponse


class ServiceNetwork:
    def __init__(self, yoga_network: YogaNetwork = Depends(YogaNetwork)):
        self.yoga_network = yoga_network

        with open("./server/services/network/translate.json", "r", encoding="utf-8") as file:
            self.interpretate_predict = json.load(file)

    def _base64ToImage(self, image_string):
        image_data = base64.b64decode(image_string.split(',')[1])
        image = Image.open(BytesIO(image_data))

        now = datetime.now()
        timestamp = int(now.timestamp() * 1000)
        fileName = f"./images_for_predict/image{timestamp}.png"

        image.save(fileName)

        return f"image{timestamp}.png"

    def predict(self, image) -> PredictGetResponse:
        fileName = self._base64ToImage(image)
        answer = self.yoga_network.predict(fileName)

        return PredictGetResponse(
            answer_english=self.interpretate_predict[answer]["english"],
            answer_russian=self.interpretate_predict[answer]["russian"]
        )
