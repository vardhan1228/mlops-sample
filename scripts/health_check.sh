#!/bin/bash

URL="http://localhost:5000"

echo "🔎 Checking app health at $URL..."

STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS_CODE" -eq 200 ]; then
    echo "✅ Health check passed!"
    exit 0
else
    echo "❌ Health check failed with status $STATUS_CODE"
    exit 1
fi