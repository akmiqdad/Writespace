# Writespace

Basic blog site written in Django (as part of project bash by TinkerWeek.py).
View Demo at: https://writespace.herokuapp.com/

## Quick Start

To get this project up and running locally on your computer:

1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic
   python manage.py createsuperuser # Create a superuser
   python manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site.
1. Open tab to `http://127.0.0.1:8000` to see the main site.
