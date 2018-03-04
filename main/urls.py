from django.urls import path

from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('build-profile/<user_id>', views.build_profile, name="build-profile"),
    path('user/<user_id>/select-strategy', views.select_strategy, name="select-strategy"),
]
