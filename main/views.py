from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def splash(request):
    context = {}
    return render(request, 'main/splash.html', context)

def login(request):
    context = {}
    return HttpResponse("You've reached login")

def signup(request):
    if request.method == "GET":
        context = {}
        return render(request, 'main/signup.html', context)
    elif request.method == "POST":
        # Create a new user object
        # Redirect to build_profile
        user_id = 1
        return redirect('/build-profile/{}'.format(user_id))


def build_profile(request, user_id):
    if request.method == "GET":
        context = {}
        return render(request, 'main/build-profile.html', context)
    elif request.method == "POST":
        # Update new user object
        # Redirect to select strategy
        return redirect('/user/{}/select-strategy'.format(user_id))

def select_strategy(request, user_id):
        context = {}
        return HttpResponse("You've reached select strategy")
