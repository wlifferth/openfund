from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def splash(request):
    context = {}
    return render(request, 'main/splash.html', context)

def login(request):
    context = {}
    return HttpResponse("You've reached login")

def signup(request):
    context = {}
    return HttpResponse("You've reacached signup")
