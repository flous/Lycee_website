from django.urls import path
from .views import adduser , sigin_user , signout_user, profile, ProfileUpdate
from django.contrib.auth.views import LoginView, LogoutView 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns  = [
    path('signup/', adduser , name='signup'),
    path('login/', sigin_user , name='login'),
    path('logout/', signout_user , name='logout'),
    path('profile/', profile , name='profile'),
    path('profile_update/', ProfileUpdate , name='profile_update'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)