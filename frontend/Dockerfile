FROM node:lts-alpine

WORKDIR /app/frontend

ENV PATH /app/frontend/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.13 -g
RUN npm install http-server -g

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN export NODE_OPTIONS=--openssl-legacy-provider
RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]
