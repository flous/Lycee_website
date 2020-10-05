from django.urls import path, include
from .views import levels,branches,modules,videos,VideoCreateView,VideoUpdateView,VideoDeleteView

urlpatterns = [
    path('levels/', levels,name='levels'),
    path('branches/<int:level_id>', branches,name='branches'),
    path('modules/<int:branche_id>', modules,name='modules'),
    path('videos/<int:module_id>', videos,name='videos'),
    path('add_videos',VideoCreateView.as_view(),name='add_videos'),
    path('update_videos/<slug:pk>/update',VideoUpdateView.as_view(),name='update_videos'),
    path('videos/<slug:pk>/delete' ,VideoDeleteView.as_view() , name='delete_videos'), 
]