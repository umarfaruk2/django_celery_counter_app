from celery import shared_task
from .models import TaskModel, CounterHistory
from django.utils import timezone
from celery.schedules import crontab
from django_celery_counter_app.celery import app

@shared_task
def add_value(amount):
    if not isinstance(amount, int):
        current_value = TaskModel.objects.all().first()
        create_history = CounterHistory.objects.create(history = current_value.value, date = timezone.now())
        print('This function only accepts integer values for amount.')
        return 

    current_value = TaskModel.objects.all().first()
    current_value.value += amount
    current_value.save()



app.conf.beat_schedule = {
    'every_10_minute': {
       'task': 'my_app.tasks.add_value',
       'schedule': crontab(minute='*/10'),
       'args': ('0',)
    }
}

