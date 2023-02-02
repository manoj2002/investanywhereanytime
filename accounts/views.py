from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import Profile
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username taken")
            elif User.objects.filter(email=email).exists():
                print('email already taken')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
        else:
            print('password not matching.....')
        return redirect('/')
    else:
        return render(request,'accounts/register.html',{'title':'IAA-Register'})

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.success(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html',{'title':'IAA-Login'})

def logout(request):
    auth.logout(request)
    return redirect('/')
def profile(request):
    if request.method=='POST':
        photo=request.FILES
        img=photo.get('img_profile')
        username=request.POST['username']
        p= Profile.objects.all()
        c=0
        for i in p:
            if i.username==username:
                if img is not None:
                    i.img=img
                    i.save()
                    c=1
                    return render(request, 'accounts/profile.html', {'title': 'IAA-Profile', 'im': i})

        if c==0:
            if img is not None:
                pi=Profile(img=img,username=username)
                pi.save()
                return render(request,'accounts/profile.html',{'title':'IAA-Profile','im':pi})
        else:
            return render(request, 'accounts/profile.html', {'title': 'IAA-Profile'})

    if request.user.is_authenticated:
        p = Profile.objects.all()
        im=None
        username = request.user.username
        for i in p:
            if i.username==username:
                im=i
                print(i.username+" "+str(i.img))
                break
        return render(request,'accounts/profile.html',{'title':'IAA-Profile','im':im})
    else:
        return redirect('login')