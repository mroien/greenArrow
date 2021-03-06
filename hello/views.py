from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Greeting

from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        #return render(request, 'live_news_links.html')
        return HttpResponseRedirect(reverse('live_news_links', args=[]))
    else:
        # return HttpResponse('Hello from Python!')
        return render(request, 'index.html')


def live_map(request):
    return render(request, 'map.html')


def live_news_links(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'live_news_links.html')
    else:
        return render(request, 'index.html')


def live_stream(request):
    return render(request, 'live_stream.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

