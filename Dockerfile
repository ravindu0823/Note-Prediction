# syntax=docker/dockerfile:1

FROM python:3.11.7

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN cat requirements.txt | xargs -n 1 -L 1 pip install --no-cache-dir
RUN apt-get update
RUN apt-get -y install ffmpeg

RUN echo "PYTHON_ENV=PRODUCTION" > .env
RUN echo "PORT=5000" >> .env

ENV PYTHON_ENV=PRODUCTION
ENV PORT=5000

COPY . .

EXPOSE 5000:5000

CMD [ "python", "-m" , "app-production"]