defaults = {
    'FORMAT': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'OUTPUT': '/youtube-dl/%(title)s.%(ext)s',
}

import youtube_dl
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from redis import Redis

app = Flask(__name__)
cors = CORS(app, resources={r"/youtube_dl/*": {"origins": "*"}})
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/youtube_dl/q', methods = ['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True, expose_headers=["Content-Disposition"])
def call():
    url = request.json.get("url")
    options = {
        'format': request.json.get("format")
    }

    if not url:
        return {"error": "No url provided"}

    download(url)
    filename = "Little Wing-Rj_NUS9hwxA.webm"

    return send_file("/code/" + filename, attachment_filename=filename, as_attachment=True)

def download(url):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download([url])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)