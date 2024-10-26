FROM python:3.11-slim-buster

WORKDIR /app

COPY . .

RUN apt update -y && \
    apt install -y git

RUN python3 -m venv venv && \
    pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PORT=1918

ENTRYPOINT [ "python3", "/app/gamma.py" ]