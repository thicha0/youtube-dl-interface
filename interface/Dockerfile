# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /interface

# add `/app/node_modules/.bin` to $PATH
ENV PATH /interface/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /interface/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

# start app
CMD ["npm", "run", "serve"]