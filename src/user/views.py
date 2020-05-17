from django.shortcuts import render, redirect
from .forms import AddUserForm , SigninForm , UserUpdateForm , ProfileUpdateForm
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
import os

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
def ProfileUpdate(request):
    if request.method == 'POST':        
        user_form =UserUpdateForm(request.POST , instance=request.user)
        image_form =ProfileUpdateForm(request.POST , request.FILES, instance=request.user.profile)
        if user_form.is_valid and image_form.is_valid :
            user_form.save()
            img=request.user.profile.image
            image_form.save()
            if img.name != 'default/default.jpg':
                try:
                    os.remove(img.path)
                except OSError as error: 
                    pass                                  
                    
            messages.success(request,'تم تعديل الملف الشخصي بنجاح ')
            return redirect('profile')
    else:
        user_form =UserUpdateForm(instance=request.user)
        image_form =ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': 'تعديل الملف الشخصي ',
        'user_form':user_form,
        'image_form':image_form,}
    return render( request , 'user/profile_Update.html' , context)