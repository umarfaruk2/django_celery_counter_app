from celery import shared_task
from .models import TaskModel
from celery.schedules import crontab
from django_celery_counter_app.celery import app

@shared_task
def add_value(amount):
    if not isinstance(amount, int):
        raise ValueError('This is accept value type')

    current_value = TaskModel.objects.all().first()
    current_value.value += amount
    current_value.save()



app.conf.beat_schedule = {
    'every_10_minute': {
       'task': 'my_app.tasks.add_value',
       'schedule': crontab(minute='*/10'),
       'ages': ('0')
    }
}

