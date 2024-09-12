from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm

def home(request):
    #check to log in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authendicate
        user = authenticate(request, username=username ,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been succesfully logedin")
            return redirect('home')
        else:
            messages.success(request,"username or password is wrong please try again....")
            return redirect('home')
    else:
        return render(request,'home.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request,"succesfully logged out")
    return redirect('home')

def register_user(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"you have been succesfully registed wellcome..!")
                return redirect('home')
    else:
        form=SignUpForm()
        return render(request,"register.html",{'form':form})
    
    return render(request,"register.html",{'form':form})

