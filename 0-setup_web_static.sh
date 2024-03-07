#!/usr/bin/env bash
# This script sets up a web server

apt-get -y update > /dev/null 2>&1
apt-get -y install nginx > /dev/null 2>&1

if ! test -d "/data"; then
        mkdir "/data"
fi

if ! test -d "/data/web_static"; then
        mkdir "/data/web_static"
fi

if ! test -d "/data/web_static/releases"; then
        mkdir "/data/web_static/releases"
fi

if ! test -d "/data/web_static/shared"; then
        mkdir "/data/web_static/shared"
fi

if ! test -d "/data/web_static/releases/test"; then
        mkdir "/data/web_static/releases/test"
fi

if ! test -f "/data/web_static/releases/test/index.html"; then
        touch "/data/web_static/releases/test/index.html"
fi

ln -sf "/data/web_static/releases/test" "/data/web_static/current"

chown ubuntu:ubuntu "/data"

config="location /hbnb_static/ {\n\
        alias /data/web_static/current/;\n\
        autoindex off;\n\
        }\n\
"

sed -i "47i\\$config" "/etc/nginx/sites-available/default"

service nginx restart > /dev/null 2>&1

exit 0
