app_defaults = {
    'FORMAT': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'AUDIO_FORMAT': None,
    'AUDIO_QUALITY': '192',
    'OUTPUT': '/youtube-dl/%(title)s [%(id)s].%(ext)s',
    'YDL_SERVER_HOST': '0.0.0.0',
    'PORT': 5000,
}

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)