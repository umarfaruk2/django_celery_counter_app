from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from .models import TaskModel, CounterHistory
from .serializers import TaskSerializer, CounterHistorySerializer
from .tasks import add_value


class TaskView(APIView):
    def get(self, request, format=None):
        history = CounterHistory.objects.all() 
        serializer = CounterHistorySerializer(history, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        json_data = request.data
        value = json_data.get('value')

        if value is not None:
            result = add_value.delay(value)
            print(f"Received value: {value} and celery result: {result}")

        return Response({'success': 'success'}) 

        
        
