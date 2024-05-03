#!/usr/bin/env bash
#  Bash script that sets up the web servers for the deployment of web_static
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo chmod 777 /data/web_static/releases/test
echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu /data/
chgrp ubuntu /data/
sed -i '26i\	location /hbnb_static {\n\t alias /data/web_static/current/;\n} ' /etc/nginx/sites-available/default
