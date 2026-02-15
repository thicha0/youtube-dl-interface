<p align="center">
    <img src="interface/assets/logo.png" alt="Logo" width="256">
</p>

# youtube-dl-interface

Download YouTube videos easily with a simple web interface.

Based on [yt-dlp](https://github.com/yt-dlp/yt-dlp) (youtube-dl fork).

## Features

- Download single YouTube videos as MP4 (video) or MP3 (audio)
- Download playlists as zip archive
- UTF-8 character support

## Structure

```
├── interface/   # Simple HTML/CSS/JS frontend
└── server/        # Flask API backend
```

## Requirements

- Python 3.x + pip
- ffmpeg (for audio conversion)
- Docker (optional)

## Quick Start

```bash
# Start server locally
make start-server

# Or with Docker
make start-server-docker

# Stop Docker container
make stop-server-docker
```

Then open `interface/index.html` in your browser.

## References

- yt-dlp: https://github.com/yt-dlp/yt-dlp
- youtube-dl: https://github.com/ytdl-org/youtube-dl
