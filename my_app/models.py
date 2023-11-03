from django.db import models

class TaskModel(models.Model):
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

class CounterHistory(models.Model):
    history = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.history)