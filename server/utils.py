app_defaults = {
    'OUTPUT': '/youtube_dl/downloads/%(title)s.%(ext)s',
    'VIDEO_QUALITY': 480,
}

import yt_dlp
import os
from collections import ChainMap
from zipfile import ZipFile

def validURL(url):
    return url.startswith((
        'https://www.youtube.com/watch?v=',
        'https://www.youtube.com/playlist?list='
    ))

def formatFilename(filename):
    for ch in ['/', '"', "|"]:
        filename = filename.replace(ch, '_')
    for ch in [":", "..."]:
        filename = filename.replace(ch, '')
    for ch in ['.']:
        if filename.startswith(ch):
            filename = '_' + filename
    return filename

def getOptions(options):
    format = options.get('format')

    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    if format == 'video':
        options = {
            'format': 'bestvideo[height=%s]+bestaudio/best' % os.getenv('VIDEO_QUALITY', app_defaults['VIDEO_QUALITY']),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }

    return {
        'format': options['format'],
        'postprocessors': options['postprocessors'],
        'outtmpl': app_defaults['OUTPUT'],
        'noplaylist' : True,
        'ignoreerrors' : True,
        'encoding' : 'utf-8',
    }

def download(url, request_options):
    with yt_dlp.YoutubeDL(getOptions(request_options)) as ydl:
        return ydl.extract_info(url, download=True)

def zipEntries(entries, name, ext):
    file_paths = []
    print("Starting zipping of entries", flush=True)
    for entry in entries:
        filename = formatFilename(entry['title'])
        try:
            file_paths.append(filename + '.' + ext)
        except Exception as e:
            print('File not found: ' + filename + '.' + ext)

    with ZipFile('/youtube_dl/downloads/' + name + '.zip', 'w') as zip:
        for file in file_paths:
            zip.write('/youtube_dl/downloads/' + file, file)