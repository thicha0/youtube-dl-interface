def validURL(url):
    return url.startswith((
        'https://www.youtube.com/watch?v=',
        'https://www.youtube.com/playlist?list='
    ))

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
        'encoding' : 'utf-8',
    }

def download(url, request_options):
    with youtube_dl.YoutubeDL(getOptions(request_options)) as ydl:
        return ydl.extract_info(url, download=True)

def zipEntries(entries, name, ext):
    file_paths = []
    print("Starting zipping of entries", flush=True)
    for entry in entries:
        file_paths.append(entry['title'].replace('/','_') + '.' + ext)

    with ZipFile('/youtube_dl/downloads/' + name + '.zip', 'w') as zip:
        for file in file_paths:
            zip.write('/youtube_dl/downloads/' + file, file)