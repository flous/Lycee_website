from django.shortcuts import render ,get_object_or_404 ,redirect , HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView ,UpdateView , DeleteView
from .models import TypeActivities , Activities , ImagesActivities
from .forms import AddActtForm
from django.contrib.auth.models import User ,Group
from django.urls import reverse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views import View

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
    paginator = Paginator(acts , 2)
    page = request.GET.get('page')
    try:
        acts=paginator.page(page)
    except PageNotAnInteger:
        acts=paginator.page(1)
    except EmptyPage:
        acts=paginator.page(paginator.num_page)
    context={
        'title':tyep_acts.title,
        'acts':acts,
        'type_act':tyep_acts,
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
class ActCreateView(LoginRequiredMixin ,UserPassesTestMixin,CreateView ):
    model = Activities
    template_name = 'ECAs/add_act.html'
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
        try:
            group =  Group.objects.get(name='member')
        except Group.DoesNotExist:
            return False
        return group in self.request.user.groups.all()

class Uplaod_images(LoginRequiredMixin,UserPassesTestMixin,View):
    def get(self, request,id_act, *args, **kwargs):
        context={'title':'تحميل صور النشاط ','act':id_act,}
        return render(request , 'ECAs/Uplaoder_images.html',context)
    def post(self, request,id_act,*args, **kwargs):
        act = Activities.objects.get(id=id_act)
        files = request.FILES.getlist('file-input')
        for f in files:
            instance = ImagesActivities(image=f , activitie=act)
            instance.save()
        return HttpResponseRedirect(reverse('act_detail', args=[id_act]))
    def test_func (self):
        try:
            group =  Group.objects.get(name='member')
        except Group.DoesNotExist:
            return False
        return group in self.request.user.groups.all()
class Delete_images(LoginRequiredMixin,UserPassesTestMixin,View):
    def get(self, request,id_act, *args, **kwargs):
        return HttpResponseRedirect(reverse('act_detail', args=[id_act]))
    def post(self, request,id_act,*args, **kwargs):
        act=Activities.objects.get(id=id_act)
        images=ImagesActivities.objects.filter(activitie=act)
        for img in images:
            if request.POST.get(str(img.pk)):
                img.delete()
        return HttpResponseRedirect(reverse('act_detail', args=[id_act]))
    def test_func (self):
        try:
            group =  Group.objects.get(name='member')
        except Group.DoesNotExist:
            return False
        return group in self.request.user.groups.all()
