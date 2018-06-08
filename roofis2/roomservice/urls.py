from django.urls import path
from . import views

app_name = 'roomservice'
urlpatterns = [
    path('', views.home, name='home'),
]
