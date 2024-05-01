from pydantic import BaseModel


class PredictGetRequest(BaseModel):
    image: str


class PredictGetResponse(BaseModel):
    answer_english: str
    answer_russian: str
