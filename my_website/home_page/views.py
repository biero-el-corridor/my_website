from importlib.metadata import requires
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request): 
    return render(request, 'home_page/home_page.html')