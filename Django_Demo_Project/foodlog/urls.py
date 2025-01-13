from django.urls import path
from . import views

app_name = 'foodlog'

urlpatterns = [
    path('', views.food_list, name='foodlog_list'),
]