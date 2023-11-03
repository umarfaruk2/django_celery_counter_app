import os
from celery import Celery
# from my_app.models import TaskModel

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_counter_app.settings')
app = Celery('django_celery_counter_app')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
