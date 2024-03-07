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

html_contain="<html>\n\
  <head>\n\
  </head>\n\
  <body>\n\
    Holberton School\n\
  </body>\n\
</html>"

echo -e "$html_contain" | tee -a "/data/web_static/releases/test/index.html" > /dev/null

ln -sf "/data/web_static/releases/test" "/data/web_static/current"

chown ubuntu:ubuntu "/data"

config="\
        location /hbnb_static/ {\n\
                alias /data/web_static/current/;\n\
                autoindex off;\n\
                }\n\
"

if ! grep -q "location /hbnb_static/" "/etc/nginx/sites-available/default"; then
        sed -i "47i\\$config" "/etc/nginx/sites-available/default"
fi

service nginx restart > /dev/null 2>&1

exit 0
