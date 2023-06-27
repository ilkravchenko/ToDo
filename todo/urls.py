from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
]
