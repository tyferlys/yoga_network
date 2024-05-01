from fastapi import APIRouter, Depends

from server.routers.network.schemas.PredictRequest import PredictGetRequest, PredictGetResponse
from server.services.network.ServiceNetwork import ServiceNetwork

routerNetwork = APIRouter()


@routerNetwork.post("/predict")
def predict(image: PredictGetRequest, service_network: ServiceNetwork = Depends(ServiceNetwork)) -> PredictGetResponse:
    answer = service_network.predict(image.image)
    return answer
