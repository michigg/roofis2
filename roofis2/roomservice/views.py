from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.jinja', {"title":"roofis is love roofis is live"})
