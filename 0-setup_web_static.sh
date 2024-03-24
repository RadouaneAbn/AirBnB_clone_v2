#!/usr/bin/env bash
# This script sets up a web server

sudo apt-get -y update > /dev/null
sudo apt-get -y install nginx > /dev/null

if ! test -d "/data"; then
        sudo mkdir "/data"
fi

if ! test -d "/data/web_static"; then
        sudo mkdir "/data/web_static"
fi

if ! test -d "/data/web_static/releases"; then
        sudo mkdir "/data/web_static/releases"
fi

if ! test -d "/data/web_static/shared"; then
        sudo mkdir "/data/web_static/shared"
fi

if ! test -d "/data/web_static/releases/test"; then
        sudo mkdir "/data/web_static/releases/test"
fi

html_contain="<html>\n\
  <head>\n\
  </head>\n\
  <body>\n\
    Holberton School\n\
  </body>\n\
</html>"

echo -e "$html_contain" | sudo tee -a "/data/web_static/releases/test/index.html"

if ! test -h "/data/web_static/current"; then
        echo rm "/data/web_static/current"
fi

sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"

sudo chown -R ubuntu:ubuntu "/data/"

config="\
        location /hbnb_static/ {\n\
                alias /data/web_static/current/;\n\
                index index.html;\n\
                }\n\
"

if ! grep -q "location /hbnb_static/" "/etc/nginx/sites-available/default"; then
        sudo sed -i "47i\\$config" "/etc/nginx/sites-available/default"
fi

sudo service nginx restart
