from roomservice.models import Room, Favorite, Booking, Staff
from .forms import FavoriteForm
import datetime
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def search(request):
    rooms = Room.objects.all()
    return render(request, 'search.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!", "rooms": rooms})


def booking(request):
    room_id = request.POST["room"]
    room = Room.objects.get(id=room_id)
    startdate = datetime.date.today()
    weekday = startdate.weekday()
    logger.info(weekday)
    enddate = startdate + datetime.timedelta(7)
    multd = []
    bookings = Booking.objects.filter(room_id=room.id, start_date__gte=startdate, end_date__lte=enddate)
    logger.info(bookings)
    for booking in bookings:
        logger.info(booking)
        sdate = booking.start_date
        logger.info(sdate)
        edate = booking.end_date
        logger.info(edate)
        stime = booking.start_time.hour
        logger.info(stime)
        etime = booking.end_time.hour + 1
        logger.info(etime)
        if edate != sdate:
            break
        else:
            if weekday == 0:
                day = "Monday"
            elif weekday == 1:
                day = "Tuesday"
            elif weekday == 2:
                day = "Wednesday"
            elif weekday == 3:
                day = "Thursday"
            elif weekday == 4:
                day = "Friday"
            elif weekday == 5:
                day = "Saturday"
            elif weekday == 6:
                day = "Sunday"
            timediff = etime - stime
            if timediff > 1:
                while timediff > 1:
                    multd.append(day + (stime + timediff - 1).__str__() + "-" + (stime + timediff).__str__())
                    timediff = timediff - 1
            logger.info(multd)
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!", "multd": multd})


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
