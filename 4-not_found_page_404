#!/usr/bin/env bash
# Configures a new ubuntu machine by installing
# Nginx where it should be listening on port 80
# Serve a page that would return a Hello World string
#

echo -e "Updating and installing Nginx.\n"
sudo apt-get update -y -qq && \
	 sudo apt-get install nginx -y

echo -e "\nSetting up some minor stuff.\n"

# starting nginx service
sudo service nginx start

# allowing nginx on firewall
sudo ufw allow 'Nginx HTTP'

# Give the user ownership to website files for easy editing
sudo chown -R "$USER":"$USER" /var/www/html
sudo chmod -R 755 /var/www

# Backup default index
cp /var/www/html/index.nginx-debian.html /var/www/html/index.nginx-debian.html.bckp

# Creating new index
echo -e "Hello World!" > /var/www/html/index.nginx-debian.html

# Setting up /redirect_me to a youtube video
sudo sed -i '24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default

# Set up a 404 page
echo "Ceci n'est pas une page" >> /var/www/html/error_404.html
sudo sed -i '25i\	error_page 404 /error_404.html;' /etc/nginx/sites-available/default

# Restarting nginx
sudo service nginx restart

echo -e "\nCompleted.\n"
