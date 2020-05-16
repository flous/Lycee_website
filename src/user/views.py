from django.shortcuts import render, redirect
from .forms import AddUserForm , SigninForm
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def adduser(request):
    if request.method == 'POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            user_name=form.cleaned_data['username']
            messages.success(request,'تهانينا "{}" لقد تمت عمليت تسجيلك بنجاح '.format(user_name))
            return redirect('login')
    else:
        form=AddUserForm()
    return render(request , 'user/sign_up.html',{'title':'التسجيل','form':form})     

# Create your views here.
def sigin_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('profile')
        else:
            messages.warning(request , '!!! هناك خطأ في إسم المستخدم أو كلمة المرور.')
    return render(request , 'user/login.html',{'title':'تسجيل الدخول '})

def signout_user (request):
    logout(request)
    return render(request , 'user/logout.html',{'title':'تسجيل الخروج '})
@login_required(login_url='login')
def profile(request):
    posts= Post.objects.filter(author=request.user)
    nbrposts = posts.count()
    paginator = Paginator(posts , 5)
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_page)
    context ={
       'title':'الملف الشخصي',
       'posts':posts,
       'nbrposts':nbrposts,
    }
    return render (request , 'user/profile.html' , context)
