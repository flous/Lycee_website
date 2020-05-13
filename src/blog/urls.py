from django.urls import path
from .views import blogs_home ,about
urlpatterns =[
    path ('',blogs_home , name='blogs'),
    path ('about/',about , name='about'),
]