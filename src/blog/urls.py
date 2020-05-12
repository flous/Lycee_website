from django.urls import path
from .views import blogs_home
urlpatterns =[
    path ('',blogs_home , name='home'),
]