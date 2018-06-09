from django.urls import path
from . import views

app_name = 'roomservice'
urlpatterns = [
    path('', views.favorites, name='home'),
    path('adminpage', views.admin, name='admin'),
    path('booking', views.booking, name='booking'),
    path('search', views.search, name='search'),
]
