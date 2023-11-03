from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'task', views.AddTaskView,basename="task")

urlpatterns = [
    path('counter/', views.TaskView.as_view())
    # path('', include(router.urls))
]
