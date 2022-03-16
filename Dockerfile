FROM ubuntu:20.04

RUN apt-get update && apt-get install python3 python3-pip -y

COPY main.py requirements.txt ./

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]





