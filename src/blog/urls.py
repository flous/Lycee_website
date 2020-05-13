from django.urls import path
from .views import blogs_home ,about , post_detail
urlpatterns =[
    path ('',blogs_home , name='blogs'),
    path ('about/',about , name='about'),
    path('detail/<int:post_id>' , post_detail , name='detail'),
]