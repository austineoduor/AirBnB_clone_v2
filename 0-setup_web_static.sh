#!/usr/bin/env bash
# Installs, configures, and starts the web server
server_config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;

	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}

	if (\$request_filename ~ redirect_me) {
		rewrite ^ https://www.holbertonschool.com/ permanent;
	}

	location = /404.html {
		root /var/www/error/;
		internal;
	}
}"
HOME_PAGE="<!DOCTYPE html>
<html lang='en-US'>
	<head>
		<title>Home - AirBnB Clone</title>
	</head>
	<body>
		<h1>Welcome to AirBnB!</h1>
	<body>
</html>
"
# shellcheck disable=SC2230
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
    apt-get update
    apt-get -y install nginx
fi
sudo mkdir -p /var/www/html /var/www/error
sudo chmod -R 755 /var/www
sudo echo 'Hello World!' > /var/www/html/index.html
sudo echo -e "Ceci n\x27est pas une page" > /var/www/error/404.html

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo -e "$HOME_PAGE" > /data/web_static/releases/test/index.html
[ -d /data/web_static/current ] && rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
echo -e '$sever_config' > /etc/nginx/sites-available/default
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
fi
