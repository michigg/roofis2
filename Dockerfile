FROM alpine:3.10

ENV UNIVIS_API_VERSION master

RUN apk --no-cache add uwsgi uwsgi-python3 py3-flask nginx python3 nginx

RUN adduser -D -g 'www' www

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt \
    && rm /requirements.txt

COPY nginx.conf /etc/nginx
COPY start.sh /
RUN chmod +x /start.sh

WORKDIR app
COPY src .
COPY src/templates/legal /tmp/legal
VOLUME ["/app/templates/legal"]


RUN mkdir /run/nginx \
    && touch /run/nginx/nginx.pid \
    && chown www:www -R . /var/log/nginx /var/lib/nginx /var/tmp/nginx /run/nginx \
    && setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/nginx

USER www

CMD ["/start.sh"]