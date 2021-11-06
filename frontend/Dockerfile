FROM node:lts-alpine

WORKDIR /app/frontend

ENV PATH /app/frontend/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.13 -g

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN export NODE_OPTIONS=--openssl-legacy-provider
RUN npm run build
EXPOSE 8080
CMD [ "npx", "http-server", "dist" ]
