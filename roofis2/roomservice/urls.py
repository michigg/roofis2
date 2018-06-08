from django.urls import path
from . import views

app_name = 'roomservice'
urlpatterns = [
    path('', views.home, name='home'),
    path('adminpage', views.admin, name='admin'),
    path('booking', views.booking, name='booking'),
]
