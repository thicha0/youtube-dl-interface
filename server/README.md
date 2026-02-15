# Server

Flask API for downloading YouTube videos.

## Run with Docker

```bash
docker build -t youtube-dl-server .
docker run -p 5000:5000 youtube-dl-server
```

For detached mode:
```bash
docker run -d -p 5000:5000 youtube-dl-server
```

## Run without Docker

Requires Python and ffmpeg.

1. Install ffmpeg: https://ffmpeg.org/download.html

2. Install dependencies and run:
```bash
pip install -r requirements.txt
python app.py
```

Server runs on `http://localhost:5000`

## API

**POST /youtube_dl/q**

```json
{
  "url": "https://www.youtube.com/watch?v=...",
  "format": "video" | "audio"
}
```

Returns: Binary file with `x-filename` header
