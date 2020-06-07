from django.shortcuts import render,get_object_or_404
from .models import Level,Branch

# Create your views here.
def levels(request):
    levels=Level.objects.all()
    context={
        'title':'المستوايات ',
        'levels':levels,
    }
    return render(request , 'videos/levels.html',context)
def branches(request , level_id):
    level=get_object_or_404(Level , pk=level_id)
    branches=level.branches.all()
    context={
        'title':'الشعب ',
        'branches':branches,
    }
    return render(request , 'videos/branches.html',context)
def modules(request , branche_id):
    branche=get_object_or_404(Branch , pk=branche_id)
    modules=branche.modules.all()
    context={
        'title':'المواد ',
        'modules':modules,
    }
    return render(request , 'videos/modules.html',context)

