#!/bin/bash
set -xe

# Set your S3 bucket and folder path
S3_BUCKET="ece461project2-webappdeploymentbucket-1kv8j892axxhq"
S3_FOLDER="project-code/"

# Set your destination folder
DESTINATION_FOLDER="~/project-code"

# Copy the entire GitHub repository code from S3 to the local folder
#aws s3 sync s3://$S3_BUCKET/$S3_FOLDER $DESTINATION_FOLDER

cd /home/ubuntu/apps
sudo apt-get clean
sudo npm cache clean --force
#scp ../environment-files/package.json .
scp ../environment-files/keys.env Elysium_Backend/keys.env
cd Elysium_Backend
pip install -r requirements.txt
python manage.py makemigrations >> makemigrations.log 2>&1
python manage.py migrate >> migrate.log 2>&1
cd ..
cd elysium_frontend
npm install >> npm-install.log 2>&1
#npm install
#rm -rf /home/ubuntu/apps/src/frontend
#scp -r build/* /var/www/build
#scp /home/ubuntu/environment-files/.env ./
#sudo apt-get clean
#sudo npm cache clean --force
#sudo rm -rf /usr/lib/node_modules/pm2
#sudo npm install -g pm2
#tsc
#sudo rm -rf /home/ubuntu/.npm
#sudo rm -rf /home/ubuntu/apps/tests