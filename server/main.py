from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.routers.network.RouterNetwork import routerNetwork

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerNetwork, prefix="/network")


@app.get("/")
def root():
    return "Сервер работает"
