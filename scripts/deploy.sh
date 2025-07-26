#!/bin/bash

APP_DIR=~/mlapp
BACKUP_DIR=~/mlapp_backup

echo "🚨 Stopping old app..."
pkill -f app.py || echo "No app was running."

echo "🛠️ Backing up current app..."
rm -rf $BACKUP_DIR
cp -r $APP_DIR $BACKUP_DIR

echo "📦 Installing dependencies..."
cd $APP_DIR
pip3 install -r requirements.txt

echo "🚀 Starting new app..."
nohup python3 app.py > output.log 2>&1 &

echo "🔍 Running health check..."
sleep 5
bash $APP_DIR/health_check.sh
STATUS=$?

if [ $STATUS -ne 0 ]; then
    echo "❌ Health check failed. Rolling back..."
    pkill -f app.py
    cp -r $BACKUP_DIR/* $APP_DIR/
    nohup python3 $APP_DIR/app.py > output.log 2>&1 &
else
    echo "✅ Deployment succeeded!"
fi