from django.shortcuts import render ,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView ,UpdateView , DeleteView
from .models import TypeActivities , Activities , ImagesActivities
from .forms import AddActtForm

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