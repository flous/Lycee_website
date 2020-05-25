from django.shortcuts import render ,get_object_or_404
from .models import TypeActivities , Activities

# Create your views here.
def Types_Activities(request):
    Types_of_activities = TypeActivities.objects.all() 
    context={
        'title':'أنواع النشاطات ',
        'Types':Types_of_activities,
    }
    return render(request , 'ECAs/Types_of_activities.html',context)
def Get_Activities(request , id_act):
    tyep_acts=get_object_or_404(TypeActivities , pk=id_act)
    acts = tyep_acts.activities.all()
    context={
        'title':'النشاطات',
        'acts':acts,
    }
    return render(request , 'ECAs/activities.html',context)
