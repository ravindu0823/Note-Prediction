# syntax=docker/dockerfile:1

FROM python:3.11.7

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN cat requirements.txt | xargs -n 1 -L 1 pip install --no-cache-dir
RUN apt-get update
RUN apt-get -y install ffmpeg

COPY . .

EXPOSE 5000:5000

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]