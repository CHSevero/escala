# The Problem
A group of doctors created a company to serve, together, a group of workstations. Previously, each of them individually attended to their own jobs, but they had difficulties taking days off as they always needed to look for
someone to cover the day of absence.
The formation of the group allowed them to define a schedule of care and each one of them can now take a day off a week.

All problem and job description (in Portuguese) is in the file DesafioDjango.pdf

## Technologies
* Python 3.9.6
    Programming language used
* Django 3.2.5
    Web development framework
* Coverage 5.5
    Library to help create automated tests.
* flake8 3.9.2
    Library to assist in adapting to pep8.
* isort 5.9.2
   Library to automatically organize imports according to pep8.
* sqlite3
    Lightweight and user-friendly relational database.
# Development environment creation
* python3.9 -m venv venv .
## Activating the development environment
* source venv/bin/activate for linux
## Requirements installation
* Go to project root
* pip install -r requirements.txt
# creating the models
* python manage.py makemigrations
* python manage.py migrate
# creating super user
* python manage.py createsuperuser
# run
* python manage.py runserver
# Project's urls
* http://127.0.0.1:8000/ doctor's scale
* http://127.0.0.1:8000/admin/ application administration
* these urls are valid on localhost
