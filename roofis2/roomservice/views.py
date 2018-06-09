from django.shortcuts import render, redirect
from roomservice.models import Room
import logging
logger = logging.getLogger(__name__)


# Create your views here.
def search(request):
    rooms = Room.objects.all()
    return render(request, 'search.jinja', {"title":"rooF(i)S is love rooF(i)S is live!!", "rooms":rooms})


def booking(request):
    room_id = request.POST["room"]
    room = Room.objects.get(id=room_id)
    logger.info(room_id)
    logger.info(room)
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!","room":room})


def admin(request):
    return render(request, 'admin.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def favorites(request):
    return render(request, 'favorites.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


