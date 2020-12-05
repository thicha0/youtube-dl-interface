Run the interface with Docker:

- `cd server`
- `docker build -t server .`
- `docker run -p 5000:5000 server` or `docker run -d -p 8080:8080 interface` for detached mode

-----

Run without Docker: (_You will need **Python** and **pip** to run this_)

- install ffpmeg: https://ffmpeg.org/download.html

- `cd server`
- `pip install --upgrade pip`
- `pip install --upgrade -r requirements.txt`
- `py app.py`