Run the interface with Docker:

- `cd interface`
- `docker build -t interface .`
- `docker run -p 8080:8080 interface` or `docker run -d -p 8080:8080 interface` for detached mode

-----

Run without Docker: (_You will need **npm** to run this_)

- `cd interface`
- `npm install`
- `npm run serve`