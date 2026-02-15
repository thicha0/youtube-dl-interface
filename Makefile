.PHONY: start-server start-server-docker stop-server-docker

start-server:
	cd server && python app.py

start-server-docker:
	cd server && docker build -t youtube-dl-server . && docker run -d --name youtube-dl -p 5000:5000 youtube-dl-server

stop-server-docker:
	docker stop youtube-dl && docker rm youtube-dl
