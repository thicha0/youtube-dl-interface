FROM python:alpine

RUN apk add --no-cache \
  ffmpeg \
  tzdata

ADD . /code
WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

CMD ["python", "app.py"]