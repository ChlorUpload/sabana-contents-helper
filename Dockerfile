FROM ubuntu:18.04
EXPOSE 80

WORKDIR /code

RUN apt-get update && \
    apt-get install -y software-properties-common

RUN apt-get update && \
    apt-get install -y python3-pip python-dev build-essential

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

RUN add-apt-repository ppa:mscore-ubuntu/mscore-stable -y
RUN apt-get update && \
    apt-get install -y musescore
RUN apt-get update && \
    apt-get install -y xvfb

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DISPLAY=:0

COPY ./ /code

CMD ["sh", "./startpoint.sh"]