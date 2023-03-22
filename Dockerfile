FROM python:3.9.16
MAINTAINER jihoon

ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=utf-8

RUN mkdir -p /home/ubuntu/mysite
RUN mkdir -p /home/ubuntu/log/gunicorn/mysite

ADD . /home/ubuntu/mysite

WORKDIR /home/ubuntu/mysite

RUN apt-get -y update && apt-get install -y \
sudo \
wget \
libgl1-mesa-glx \
libxml2-utils

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r package-1.txt

EXPOSE 8000
CMD ["sh", "on-container-start.sh"]
