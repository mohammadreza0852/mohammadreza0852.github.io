from django.shortcuts import render
from MyWeb.models import HomePage, AboutMe, Abilities
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'MyWeb/home.html')


def index(request):
    home_model = HomePage.objects.get(name=request.GET['input_text'])
    about_model = AboutMe.objects.get(name=request.GET['input_text'])
    skills = Abilities.objects.get(name=request.GET['input_text'])
    return render(request, 'MyWeb/index.html', {'x': home_model, 'y': about_model, 'my_skill': skills})


def showID(request):
    return HttpResponse(f"this is post id number ")