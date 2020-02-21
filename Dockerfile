# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY roofis2/package*.json ./
RUN npm install
COPY ./roofis2 .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./docker/roofis2/nginx.conf /temp/prod.conf
RUN envsubst /app < /temp/prod.conf > /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]