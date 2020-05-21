from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ECAs_home , Types_Activities
urlpatterns  = [
    path('activities/', ECAs_home , name='activities'),
    path('typesactivities/',Types_Activities,name='typesactivities')
    # path('login/', sigin_user , name='login'),
    # path('logout/', signout_user , name='logout'),
    # path('profile/', profile , name='profile'),
    # path('profile_update/', ProfileUpdate , name='profile_update'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)