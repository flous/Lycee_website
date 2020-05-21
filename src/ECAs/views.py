from django.shortcuts import render
from .models import TypeActivities

# Create your views here.
def ECAs_home(request):
    context = {
        'title' : 'النشاطات ',
    }
    return render(request , 'ECAs/activities.html',context)


def Types_Activities(request):
    Types_of_activities = TypeActivities.objects.all() 
    context={
        'titel':'أنواع النشاطات ',
        'Types':Types_of_activities,
    }
    return render(request , 'ECAs/Types_of_activities.html',context)