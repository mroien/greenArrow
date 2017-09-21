from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


@login_required
def live_map(request):
    return render(request, 'map.html')


def live_stream(request):
    return render(request, 'live_stream.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

