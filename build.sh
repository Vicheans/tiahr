#!/bin/bash


#Build the project
echo "Building App..."
python3.13 -m pip install -r requirements.txt

echo "Initiating Migrations..."
python3.13 manage.py makemigrations --noinput
python3.13 manage.py migrate --noinput

echo "Processing statics..."
