from django.urls import path
from .views import adduser
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns  = [
    path('signup/', adduser , name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html') , name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html') , name='logout'),
]