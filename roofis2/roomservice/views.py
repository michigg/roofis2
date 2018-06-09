from django.shortcuts import render
from roomservice.models import Room, Booking
import logging
import datetime
logger = logging.getLogger(__name__)


# Create your views here.
def search(request):
    rooms = Room.objects.all()
    return render(request, 'search.jinja', {"title":"rooF(i)S is love rooF(i)S is live!!", "rooms": rooms})


def booking(request):
    room_id = request.POST["room"]
    room = Room.objects.get(id=room_id)
    logger.info(room_id)
    logger.info(room)
    startdate = datetime.date.today()
    weekday = startdate.weekday()
    enddate = startdate + datetime.timedelta(7)
    multd = [[]]
    bookings = Booking.objects.filter(room_id=room.id, start_date__gte=startdate, end_date__lte=enddate)
    for booking in bookings:
        sdate = booking.start_date
        edate = booking.end_date
        stime = booking.start_time.hour
        etime = booking.end_time.hour+1
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
                    multd.append([day, stime + timediff])
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!", "multd":multd})


def admin(request):
    return render(request, 'admin.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def favorites(request):
    return render(request, 'favorites.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})