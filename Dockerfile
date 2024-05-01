FROM python:3.12

RUN mkdir /yoga-server
WORKDIR /yoga-server

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx

COPY . .

CMD uvicorn server.main:app --workers 4 --host 0.0.0.0 --port 8000
