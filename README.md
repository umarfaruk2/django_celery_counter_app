# django_celery_counter_app

In this project I try to implement celery with django. First we have a counter value now You provide a value in body that add in current value in every give amount request. Second our counter value store in counter_history that update in every 10 minute.  

I provide 2 endpoint ones you post a amount that update the counter current value and another one get the all counter history every 10 minute. 

Celery code you find in - `my_app.tasks.py`

### Post value that update current value
- http://127.0.0.1:8000/counter/ (post method)

### Get all counter value that update in every 10 minute
- http://127.0.0.1:8000/counter/ (get method) 


## How to start this project
- Download the project and unzip
- After download open it any code editor(In you device must have django, rest_framework, celery)
- python manage.py makemigrations(In terminal)
- python manage.py migrate(In terminal)

### Command that you have to run for see result
- python manage.py runserver
- celery -A django_celery_counter_app  worker -l info
- celery -A django_celery_counter_app  beat -l info
