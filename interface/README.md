docker build -t my-container .

docker run -it -p 8080:80 --rm --name my-container my-container

https://www.youtube.com/watch?v=N-DM9ibBXVg

docker run -v %cd%:/app -v /app/node_modules -p 8081:8080 --rm my-app:dev -it

https://mherman.org/blog/dockerizing-a-vue-app/

docker run -it -p 8081:8080 --rm --name my-app my-app:dev