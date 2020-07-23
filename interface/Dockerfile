# base image
FROM node:12.2.0-alpine

RUN apk update
RUN apk add --update python3
RUN python3 -m pip install --upgrade pip
RUN pip install --upgrade youtube-dl

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package*.json ./
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
COPY . .

# start app
CMD ["npm", "run", "serve"]