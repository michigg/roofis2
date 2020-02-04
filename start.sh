#!/usr/bin/env ash
if [ ! -f /app/templates/legal/* ]; then
    cp /tmp/legal/* /app/templates/legal/
fi

nginx
uwsgi --ini app.ini