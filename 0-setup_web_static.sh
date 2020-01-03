#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
apt-get -y update
apt-get -y install nginx
sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf
service nginx start
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Hello World" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex on;\n\t}\n/" /etc/nginx/sites-available/default
service nginx restart
exit 0
