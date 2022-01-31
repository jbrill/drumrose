FROM nginx:1.19-alpine

ENV DRUMROSE_DOMAIN 'teton.drumrose.io'

COPY ./nginx.conf.template /etc/nginx/templates/nginx.conf.template

# CMD ["/bin/sh" , "-c" , "envsubst < /nginx.conf.template > /etc/nginx/nginx.conf && exec nginx -g 'daemon off;'"]