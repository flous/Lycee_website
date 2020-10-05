from django.shortcuts import render,get_object_or_404
from .models import Level,Branch,Module,Video
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView ,UpdateView , DeleteView
from django.contrib import messages
from django.urls import reverse
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
def videos(request , module_id):
    modules=get_object_or_404(Module , pk=module_id)
    videos=modules.videos.all()
    context={
        'title':'فيديوهات ',
        'videos':videos,
    }
    return render(request , 'videos/videos.html',context)

class VideoCreateView(LoginRequiredMixin ,CreateView):
    # ينقص هنا التأكد من أن المستخدم ينتمي إلى مجموعة الأساتذة المصرح لهم
    model=Video
    fields=['title','description','link','module']
    template_name = 'videos/Add_vedio.html'
    def form_valid(self , form):
        messages.success(self.request , 'لقد تم إضافة الفيديو بنجاح')
        return super().form_valid(form)
class VideoUpdateView(LoginRequiredMixin ,UpdateView):
    model=Video
    fields=['title','description','link','module']
    template_name = 'videos/Update_vedio.html'
    def form_valid(self , form):
        messages.success(self.request , 'لقد تم إضافة الفيديو بنجاح')
        return super().form_valid(form)
class VideoDeleteView(LoginRequiredMixin ,DeleteView):
    model =Video
    def get_success_url(self):
        return reverse('videos', kwargs={'module_id': self.object.module.id})

