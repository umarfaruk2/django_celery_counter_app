from .models import TaskModel, CounterHistory
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

class CounterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterHistory
        fields = '__all__' 