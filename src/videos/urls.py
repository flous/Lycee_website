from django.urls import path, include
from .views import levels,branches,modules,videos

urlpatterns = [
    path('levels/', levels,name='levels'),
    path('branches/<int:level_id>', branches,name='branches'),
    path('modules/<int:branche_id>', modules,name='modules'),
     path('videos/<int:module_id>', videos,name='videos'),  
]