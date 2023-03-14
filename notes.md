# Django Blogger Site Notes

- django-admin startproject djblogger

## modularise settings.py
- make settings folder inside main app named djblogger
- make:
      - base.py
      - local.py
      - production.py
- insert following code to local.py and production.py
   from .base import *

- in base.py DEBUG= True is set 
- import base from djblogger.settings
- in manage.py main function:
   -  if base.DEBUG :   <br>
         os.environ........("...","djblogger.settings.local") <br>
      else:<br>
         os.environ........("...","djblogger.settings.production")<br>

## Generating secret Key
- python manage.py shell
- from django.core.management.utils import get_random_secret_key
- print(get_random_secret_key())

## Setting Environment Variables
- inside djblogger main app folder, i.e at same level of manage.py:
   make .env file
- move DEBUG and SECRET_KEY variables to .env file
- configure settings file to read from .env file:
   - in base.py:
      - import os
      - from dotenv import load_dotenv
      - load_dotenv()
      - SECRET_KEY = os.environ.get('SECRET_KEY')
      - DEBUG = os.environ.get('DEBUG') == "TRUE"

## Pytest Setup for testing purpose
- pip install pytest-django
- make pytest.ini in the main folder; same level as manage.py
- Inside pytest.ini:
   - [pytest]
   - DJANGO_SETTING_MODULE = djblogger.settings.local
   - python_files = test_*.py
   - make tests folder ; same level as other apps
   - make test_example.py:
      def test_example():
         assert 1==1
   - run pytest command in terminal to run test

## Creating Github repo 
   