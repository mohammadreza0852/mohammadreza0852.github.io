from django.shortcuts import render
from MyWeb.models import HomePage, AboutMe, Abilities

# Create your views here.

def home(request):
    home_model = HomePage.objects.all()
    about_model = AboutMe.objects.all()
    skills = Abilities.objects.all()
    return render(request, 'MyWeb/index.html', {'home_model': home_model, 'about_model': about_model, 'skill': skills})
