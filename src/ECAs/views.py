from django.shortcuts import render

# Create your views here.
def ECAs_home(request):
    context = {
        'title' : 'النشاطات ',
    }
    return render(request , 'ECAs/activities.html',context)
