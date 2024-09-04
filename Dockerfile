FROM python:3.12-slim

RUN yum update -y && \
    yum install -y git python3.12-pip 

WORKDIR /app

COPY . /app 

RUN pip install -r requirements.txt

EXPOSE 2005

CMD ["python3.12", "./gamma.py"]
