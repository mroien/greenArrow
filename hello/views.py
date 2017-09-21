from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request, 'map.html')
    else:
        # return HttpResponse('Hello from Python!')
        return render(request, 'index.html')


def live_map(request):
    return render(request, 'map.html')


def live_stream(request):
    return render(request, 'live_stream.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

