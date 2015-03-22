FROM ubuntu-debootstrap:14.04

RUN apt-get update -y \
    && apt-get install -y tar python python-dev python-distribute python-pip libmysqlclient-dev python-yaml

ADD /subscriberConsumer /subscriberConsumer

RUN pip install -r /subscriberConsumer/conSub_requires

WORKDIR /subscriberConsumer

CMD python ./src/conSub_server.py

# Expose Ports.
EXPOSE 8888
