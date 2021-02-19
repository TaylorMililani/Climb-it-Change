# Climb-it-Change
A training app for bouldering. Made with Flask, React, PostgreSQL, Google OAuth, and deployed with Heroku.
This repo contains the flask API.
This API talks to the react frontend and sends information about the current user, creates a plan for a new user, and saves the workout user's schedule.

To get the api running, in the command line run:

$ source env/bin/activate

To install dependencies:

$ pip install -r requirements.txt

To setup the tables and seed the database:

$ python3 models.py

$ python3 seeds.py
