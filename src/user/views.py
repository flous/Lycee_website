from django.shortcuts import render, redirect
from .forms import AddUserForm , SigninForm
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout


def adduser(request):
    if request.method == 'POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data['username']
            messages.success(request,'تهانينا "{}" لقد تمت عمليت تسجيلك بنجاح '.format(user_name))
            return redirect('blogs')
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
            return redirect('blogs')
        else:
            messages.warning(request , '!!! هناك خطأ في إسم المستخدم أو كلمة المرور.')
    return render(request , 'user/login.html',{'title':'تسجيل الدخول '})     

def signout_user (request):
    logout(request)
    return render(request , 'user/logout.html',{'title':'تسجيل الخروج '})    


