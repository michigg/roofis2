from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'search.jinja', {"title":"rooF(i)S is love rooF(i)S is live!!"})


def booking(request):
    return render(request, 'booking.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})


def admin(request):
    return render(request, 'admin.jinja', {"title": "rooF(i)S is love rooF(i)S is live!!"})

