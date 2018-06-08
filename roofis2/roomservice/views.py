from django.shortcuts import render
from roomservice.models import Room


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'search.jinja', {"title":"rooF(i)S is love rooF(i)S is live!!", "rooms":rooms})


def booking(request):
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def admin(request):
    return render(request, 'admin.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def favorites(request):
    return render(request, 'favorites.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})