FROM python:3.6

MAINTAINER j1b0n666

# Our application will listen on port 5000 inside the container
# so here we tell Docker that we want to expose that port to the outside
# world
EXPOSE 80

ADD . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

CMD python app.py
