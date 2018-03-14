from django.shortcuts import HttpResponse, render
from django.template import loader



def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def map(request):
    return render(request, 'glowapp/map.html')
