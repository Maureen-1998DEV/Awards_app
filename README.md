# Projects Name:
##  AWARD_APP

## Contributors
    - Maureen Ougo

### Contact Information
ougomaureen051@gmail.com
## Description
Award_app is my third project in django that enables a User to post thier projects so as to be rewarded.

## Features
- The home page allows user to login,create an Account  or activate the previous account:
- User can be able to see his/her profile ,edit and post pictures:
- Users can also see other users profile ,photos and even comment about them
- Admin can upload images from a django dashboard

## View Live Site here
View the complete site [here](https://ougo-award.herokuapp.com/)

## Technologies Used
    - Python 3.8
    - Django MVC framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku

## Specifications
To view the user dtories or BDD check the [specs file](specs.md).

### Prerequisite
MyGallery requires a prerequisite understanding of the following:

- Python3.8
- Postgres
- Python virtualenv
- Django Framework
## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE award;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'award'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations award_app
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
No known bugs so far.

# LICENCE
[MIT]([Python3](https://www.python.org/)  ) 

# &COPY;Awwwards 2021