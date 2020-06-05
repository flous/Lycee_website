from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import  Delete_images,Types_Activities , Get_Activities , act_detail , ActCreateView , ActUpdateView , ActDeletView ,Uplaod_images
urlpatterns  = [
    path('typesactivities/',Types_Activities,name='typesactivities'),
    path('activities/<int:id_act>', Get_Activities , name='activities'),
    path('act_detail/<int:id_act>', act_detail , name='act_detail'),
    path ('add_act/',ActCreateView.as_view(), name='add_act'),
    path ('update_act/<slug:pk>',ActUpdateView.as_view(), name='update_act'),
    path('delete_act/<slug:pk>' ,ActDeletView.as_view() , name='delete_act'),
    path('upload_images/<int:id_act>' ,Uplaod_images.as_view(), name='upload_images'),
    path('delete_images/<int:id_act>' ,Delete_images.as_view(), name='delete_images'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)