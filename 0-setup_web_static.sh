#!/usr/bin/env bash
# A Bash script that sets up a web server for the deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

echo "Hello World!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf %s "server {
        listen 80 default_server;

        location /hbnb_static/ {
        alias /data/web_static/current/;
        }
}
" > /etc/nginx/sites-enabled/default

service nginx restart
