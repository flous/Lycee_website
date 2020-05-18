from django.urls import path
from .views import blogs_home ,about , post_detail , PosteCreateView , PosteUpdateView , PosteDeletView
urlpatterns =[
    path ('',blogs_home , name='blogs'),
    path ('about/',about , name='about'),
    path('detail/<int:post_id>' , post_detail , name='detail'),
    path ('add_post/',PosteCreateView.as_view(), name='add_post'),
    path('detail/<slug:pk>/update' ,PosteUpdateView.as_view() , name='post-update'),
    path('detail/<slug:pk>/delete' ,PosteDeletView.as_view() , name='post-delete'),
]