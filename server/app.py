app_defaults = {
    'FORMAT': 'bestaudio/best',
    'AUDIO_FORMAT': None,
    'AUDIO_QUALITY': '192',
    'VIDEO_FORMAT': None,
    'OUTPUT': '/code/%(id)s.%(ext)s',
}

import youtube_dl
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from redis import Redis
from collections import ChainMap
import os
from zipfile import ZipFile

app = Flask(__name__)
cors = CORS(app, resources={r"/youtube_dl/*": {"origins": "*"}})
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/youtube_dl/q', methods = ['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True, expose_headers=["x-filename"])
def call():
    url = request.json.get("url")
    format = request.json.get("format")
    options = {
        'format': format
    }

    if not url:
        return {"error": "No url provided"}

    ext = 'mp4'
    if format == 'audio':
        ext = 'mp3'

    try:
        result = download(url, options)
    except:
         return {"error": "An error has occurred during the download"}, 500

    title = result['title']
    id = result['id']
    type = result.get('_type', 'video')

    if type == 'playlist':
        file_paths = []
        for entry in result['entries']:
            file_paths.append(entry['id'] + '.' + ext)

        with ZipFile(id + '.zip','w') as zip:
            for file in file_paths:
                zip.write(file)

        ext = 'zip'

    filename = id + '.' + ext

    try:
        response = send_file('/code/' + filename)
    except:
        return {"error": "An error has occurred during the sending of the file"}, 500

    response.headers['x-filename'] = title + '.' + ext
    return response

def get_ydl_options(options):

    format = options.get('format')

    if format == 'audio':
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': app_defaults['OUTPUT'],
            'noplaylist' : True,
        }

    #default = video format
    return {
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'outtmpl': app_defaults['OUTPUT'],
        'noplaylist' : True,
    }


def download(url, request_options):
    with youtube_dl.YoutubeDL(get_ydl_options(request_options)) as ydl:
        return ydl.extract_info(url, download=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)