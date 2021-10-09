FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python python-pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py /opt/
ENTRYPOINT FLASK_APP=/opt/app.py flash run --host=0.0.0.0 --port=8080