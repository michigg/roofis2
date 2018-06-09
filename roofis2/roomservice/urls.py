from django.urls import path, include
from . import views

app_name = 'roomservice'
urlpatterns = [
    path('', views.favorites, name='home'),
    path('favorite', views.add_favorites, name='add-fav'),

    path('adminpage', views.admin, name='admin'),
    path('booking', views.booking, name='booking'),
    path('search', views.search, name='search'),
    path('location_search', views.location_based_search, name='location-based-search'),
    path('filter_search', views.filter_search, name='filter-search')]

