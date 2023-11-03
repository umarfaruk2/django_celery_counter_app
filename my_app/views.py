from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import TaskModel
from .serializers import TaskSerializer
# from django_celery_counter_app.celery import add_value
from .tasks import add_value


class AddTaskView(APIView):
    def get(self, request, format=None):
        pass
    def post(self, request, format=None):
        json_data = request.data
        value = json_data.get('value')

        if value is not None:
            result = add_value.delay(value)
            print(f"Received value: {value} and celery result: {result}")

        return Response({'success': 'success'}) 

        
        
