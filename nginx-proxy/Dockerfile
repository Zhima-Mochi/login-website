FROM node:17.6.0 as builder

WORKDIR /frontend

COPY frontend-login-website/package.json frontend-login-website/package-lock.json /frontend/

RUN npm install

COPY frontend-login-website/ /frontend/

ARG REACT_APP_API

ENV REACT_APP_API $REACT_APP_API

RUN npm run public-build

FROM nginx:1.21.6

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=builder /frontend/build .

COPY nginx.conf /etc/nginx/nginx.conf