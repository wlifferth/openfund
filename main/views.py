from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile
from .updateUserProfile import updateUserProfile

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
        new_user = UserProfile(name=request.POST['name'], email=request.POST['email'], passwordHash=request.POST['password'])
        new_user.save()
        user_id = new_user.id
        # Redirect to build_profile
        return redirect('/build-profile/{}'.format(user_id))


def build_profile(request, user_id):
    context = {}
    if request.method == "GET":
        user = UserProfile.objects.filter(id=user_id).get()
        context['name'] = user.name
        return render(request, 'main/build-profile.html', context)
    elif request.method == "POST":
        print(request.POST)
        # Update new user object
        user = UserProfile.objects.filter(id=user_id).get()
        updateUserProfile(user, request.POST)
        # Redirect to select strategy
        return redirect('/user/{}/select-strategy'.format(user_id))


def select_strategy(request, user_id):
        context = {}
        return HttpResponse("You've reached select strategy")
