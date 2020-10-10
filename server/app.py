app_defaults = {
    'OUTPUT': '/youtube_dl/downloads/%(title)s.%(ext)s',
    'VIDEO_QUALITY': 480,
}

import youtube_dl
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from redis import Redis
from collections import ChainMap
import os
from zipfile import ZipFile
from flask import abort
from "utils.py" import validURL, download, zipEntries

app = Flask(__name__)
cors = CORS(app, resources={r"/youtube_dl/*": {"origins": "*"}})
redis = Redis(host='redis', port=6379)

@app.route('/youtube_dl/q', methods = ['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True, expose_headers=["x-filename"])
def call():
    url = request.json.get("url")
    format = request.json.get("format")
    options = {
        'format': format
    }

    if not url:
        return {"error": "No URL provided !"}, 400

    if not validURL(url):
        return {"error": "This URL is not valid !"}

    ext = 'mp4'
    if format == 'audio':
        ext = 'mp3'

    try:
        result = download(url, options)
    except Exception as e:
        print(e, flush=True)
        return {"error": "An error has occurred during the download. Make sure that the URL provided is correct !"}, 500

    filename = result['title'].replace('/', '_')
    type = result.get('_type', 'video')

    if type == 'playlist':
        try:
            zipEntries(result['entries'], filename, ext)
            ext = 'zip'
        except Exception as e:
            print(e, flush=True)
            return {"error": "An error has occurred during the zipping..."}, 500

    try:
        response = send_file('/youtube_dl/downloads/' + filename + '.' + ext)
    except Exception as e:
        print(e, flush=True)
        return {"error": "An error has occurred during the sending of the file..."}, 500

    response.headers['x-filename'] = (filename + '.' + ext).encode(encoding='UTF-8', errors='ignore')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)