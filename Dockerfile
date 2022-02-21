FROM python:3.6

MAINTAINER j1b0n666

# Our application will listen on port 5000 inside the container
# so here we tell Docker that we want to expose that port to the outside
# world
EXPOSE 80

ADD . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz

CMD python app.py
