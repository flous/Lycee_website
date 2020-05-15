from django.urls import path
from .views import adduser , sigin_user , signout_user, profile
from django.contrib.auth.views import LoginView, LogoutView 
urlpatterns  = [
    path('signup/', adduser , name='signup'),
    path('login/', sigin_user , name='login'),
    path('logout/', signout_user , name='logout'),
    path('profile/', profile , name='profile'),
]