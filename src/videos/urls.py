from django.urls import path, include
from .views import levels,branches,modules

urlpatterns = [
    path('levels/', levels,name='levels'),
    path('branches/<int:level_id>', branches,name='branches'),
    path('modules/<int:branche_id>', modules,name='modules'),  
]