from roomservice.models import Room, Favorite, Booking
import datetime
from django.shortcuts import render
from roomservice.models import Room
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def search(request):
    rooms = Room.objects.all()
    return render(request, 'search.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!", "rooms": rooms})


def booking(request):
    room_id = request.POST["room"]
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!","data":room_id})



def admin(request):
    return render(request, 'admin.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def favorites(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(staff__user=request.user)
        return render(request, 'favorites.jinja',
                      {"title": "rooF(i)S is love rooF(i)S is live!!", 'favorites': favorites})
    return render(request, 'favorites.jinja',
                  {"title": "rooF(i)S is love rooF(i)S is live!!"})


def add_favorites(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'add_fav.jinja', {"title": "Add a new Favorite"})


def location_based_search(request):
    return render(request, 'favorites.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def filter_search(request):
    if request.method=="POST":
        logger.info(request.POST)


    return render(request, 'search.jinja',{"title": "rooF(i)S is love rooF(i)S is live!!"})

