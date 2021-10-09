FROM python:3.6
RUN adduser usr
RUN apt-get update && apt-get install -y python python-pip
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8080
RUN chown -R usr:usr /usr/sbin/adduser
ENTRYPOINT python3 app.py
