from django.shortcuts import render ,get_object_or_404 ,redirect , HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView ,UpdateView , DeleteView
from .models import TypeActivities , Activities , ImagesActivities
from .forms import AddActtForm
from django.contrib.auth.models import User ,Group
from django.urls import reverse

# Create your views here.
# من أجل عرض أنواع النشاطات على الصفحة Types_of_activities.html 
def Types_Activities(request):
    Types_of_activities = TypeActivities.objects.all() 
    context={
        'title':'أنواع النشاطات ',
        'Types':Types_of_activities,
    }
    return render(request , 'ECAs/Types_of_activities.html',context)
    # من أجل عرض 
def Get_Activities(request , id_act):
    tyep_acts=get_object_or_404(TypeActivities , pk=id_act)
    acts = tyep_acts.activities.all()
    context={
        'title':tyep_acts.title,
        'acts':acts,
    }
    return render(request , 'ECAs/activities.html',context)
def act_detail(request , id_act):
    act=get_object_or_404(Activities , pk=id_act)
    imgs=act.images.all()
#  التتحقق في حالة إرسال البيانات من أجل إضافة تعيق خاص بمنشور معين 
    

    context={
        'title' :act.title,
        'act': act,
        'imgs_activiti':imgs,  
    }
    return render(request , 'ECAs/act_detail.html', context)
class ActCreateView(LoginRequiredMixin ,CreateView ):
    model = Activities
    template_name = 'ECAs/add_act.html'
    form_class =AddActtForm
  
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 # تعديل نشاط موجود مسبقا 
class ActUpdateView(LoginRequiredMixin ,UserPassesTestMixin,UpdateView):
    model = Activities
    template_name = 'ECAs/update_act.html'
    form_class =AddActtForm
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func (self):
        try:
            group =  Group.objects.get(name='member')
        except Group.DoesNotExist:
            return False
        return group in self.request.user.groups.all()
class ActDeletView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Activities
    success_url = '/'
    def test_func (self):
        act =self.get_object()
        if self.request.user == act.author:
            return True
        return False
def uplaod_images(request , id_act):
    if request.method=='POST':
        act = Activities.objects.get(id=id_act)
        files = request.FILES.getlist('file-input')
        for f in files:
            instance = ImagesActivities(image=f , activitie=act)
            instance.save()
        # return redirect('/act_detail/'+str(id_act))
        return HttpResponseRedirect(reverse('act_detail', args=[id_act]))
    else:
        context={'title':'تحميل صور النشاط ','act':id_act,}
        return render(request , 'ECAs/Uplaoder_images.html',context)
def delete_images(request , id_act):
    if request.method=='POST':
        act=Activities.objects.get(id=id_act)
        images=ImagesActivities.objects.filter(activitie=act)
        for img in images:
            if request.POST.get(str(img.pk)):
                img.delete()

        # return redirect('/act_detail/'+str(id_act))
        return HttpResponseRedirect(reverse('act_detail', args=[id_act]))
    else:
        context={'title':'تحميل صور النشاط ','act':id_act,}
        return render(request , 'ECAs/Uplaoder_images.html',context)