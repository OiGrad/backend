# Starting 

- to install project dependencies run `pip install -r requirements.txt`
- to run migrations run `python manage.py makemigrations`
- to run migrations run `python manage.py migrate`
- to run the project run `python manage.py runserver`
- to run tests run `python manage.py test`
- to create superuser run `python manage.py createsuperuser`
- to run celery worker run `celery -A config worker -l info`
- to run celery beat run `celery -A config beat -l info`
- to run celery flower run `celery -A config flower`
