from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect


# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username exists'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error':'Password must match'})
    else:
        return render(request, 'accounts/signup.html')
    
def login(request):
    next_url=request.GET.get('next')
    if request.method=='POST':
        user=auth.authenticate(username= request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST['next']:
                return HttpResponseRedirect(request.POST['next'])
            else:
                redirect('home')
 
        else: 
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect!','next': request.POST['next']})
    else:
        return render(request, 'accounts/login.html', {'next':next_url})
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')

    #Need to route to homepage
    #and don't forget to logout
    return render(request, 'accounts/signup.html')