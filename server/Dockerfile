FROM python:alpine

RUN apk add --no-cache \
  ffmpeg \
  tzdata

ADD . /youtube_dl
WORKDIR /youtube_dl

COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

CMD ["python", "app.py"]