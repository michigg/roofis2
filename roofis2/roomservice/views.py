from roomservice.models import Room, Favorite, Booking, Staff
from .forms import FavoriteForm
from django.shortcuts import render
from roomservice.models import Room
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def search(request):
    if request.method == 'POST':
        logger.info(request.POST)
        search_token = request.POST['search']
        rooms = Room.objects.all()
        # barrierfree = request.POST.get('barrierfree', 'off')
        # logger.info(barrierfree)
        if search_token:
            rooms = rooms.filter(room_number__contains=search_token)
        # else:
        #     # barrierfree = request.POST['barrierfree']
        #
        #     if barrierfree:
        #         # barrierfree = request.POST['barrierfree']
        #         if barrierfree == 'on':
        #             rooms = rooms.filter(barrierfree=True)
        #
        #     if 'seating' in request.POST:
        #         seating = request.POST['seating']
        #         if seating == 'on':
        #             rooms = rooms.filter(seating=True)
        #
        #     if 'cooling' in request.POST:
        #         cooling = request.POST['cooling']
        #         if cooling == 'on':
        #             rooms = rooms.filter(cooling=True)
        #
        #     if 'capatacity' in request.POST:
        #         capatacity = request.POST['capatacity']
        #         if not capatacity == '-1':
        #             rooms = rooms.filter(capacity__gte=capatacity)

        # logger.info(search_token, barrierfree, seating, cooling, capatacity)

        return render(request, 'search.jinja',
                      {"title": "rooF(i)S is love rooF(i)S is live!!", "rooms": rooms, "result_count": rooms.count()})
    else:
        rooms = {}
        return render(request, 'search.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!", "rooms": rooms})


def booking(request, id):
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!", "data": id})


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
        form = FavoriteForm(request.POST)
        if form.is_valid():
            staff = Staff.objects.get(user=request.user)
            room = form.cleaned_data['room']
            Favorite.objects.create(staff=staff, room=room)
            return render(request, 'success.jinja', {})
        else:
            return render(request, 'error.jinja', {})
    else:
        form = FavoriteForm()
        return render(request, 'add_fav.jinja', {"title": "Add a new Favorite", 'form': form})


def location_based_search(request):
    return render(request, 'favorites.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def success(request):
    return render(request, 'success.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def error(request):
    return render(request, 'error.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def filter_search(request):
    if request.method == "POST":
        logger.info(request.POST)

    return render(request, 'search.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})
