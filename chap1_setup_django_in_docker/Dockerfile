FROM python:3.10

ENV PYTHONUNBUFFERED: 1

WORKDIR /user/src/app

RUN pip install --upgrade pip

RUN pwd

COPY requirements.txt ./requirements.txt
COPY start-project.sh /user/src/app/ 

#COPY hello.py /user/src/app 

RUN pip3 install -r requirements.txt

