defaults = {
    'FORMAT': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'OUTPUT': '/youtube-dl/%(title)s.%(ext)s',
}

import youtube_dl
from flask import Flask, request, send_file
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/youtube_dl/q', methods = ['POST'])
def call():
    url = request.json.get("url")
    options = {
        'format': request.json.get("format")
    }

    if not url:
        return {"error": "No url provided"}

    download(url)
    return send_file("/code/Little Wing-Rj_NUS9hwxA.webm", attachment_filename="test", as_attachment=True)
    #return send_file("/code/Little Wing-Rj_NUS9hwxA.webm")

def download(url):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download([url])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)