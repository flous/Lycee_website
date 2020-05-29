from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import  Types_Activities , Get_Activities , act_detail , ActCreateView
urlpatterns  = [
    path('typesactivities/',Types_Activities,name='typesactivities'),
    path('activities/<int:id_act>', Get_Activities , name='activities'),
    path('act_detail/<int:id_act>', act_detail , name='act_detail'),
    path ('add_act/<slug:pk>',ActCreateView.as_view(), name='add_act'),
    # path('login/', sigin_user , name='login'),
    # path('logout/', signout_user , name='logout'),
    # path('profile/', profile , name='profile'),
    # path('profile_update/', ProfileUpdate , name='profile_update'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)