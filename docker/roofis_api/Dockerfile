FROM alpine:3.10

ENV VERSION master
ENV REPO_NAME roofis2_api

RUN apk --no-cache add uwsgi uwsgi-python3 py3-flask nginx python3 nginx
RUN adduser -D -g 'www' www

WORKDIR app

RUN wget https://github.com/michigg/roofis2_api/archive/$VERSION.zip \
    && unzip $VERSION.zip \
    && rm $VERSION.zip \
    && mv ./$REPO_NAME-$VERSION/requirements.txt /requirements.txt \
    && mv ./$REPO_NAME-$VERSION/src/* /app \
    && mv ./$REPO_NAME-$VERSION/nginx.conf /etc/nginx \
    && mv ./$REPO_NAME-$VERSION/start.sh /start.sh \
    && rm -r ./$REPO_NAME-$VERSION

#COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt \
    && rm /requirements.txt

#COPY nginx.conf /etc/nginx
#COPY start.sh /
RUN chmod +x /start.sh

#COPY src .

RUN mkdir /run/nginx \
    && touch /run/nginx/nginx.pid \
    && chown www:www -R . /var/log/nginx /var/lib/nginx /var/tmp/nginx /run/nginx \
    && setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/nginx

USER www

CMD ["/start.sh"]