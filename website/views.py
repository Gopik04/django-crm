from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm
from .models import Record
from .form import AddRecordForm

def home(request):
    #retrive the data from database:
    records=Record.objects.all() 
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
        return render(request,'home.html',{'records':records})

#for logout 
def logout_user(request):
    logout(request)
    messages.success(request,"succesfully logged out")
    return redirect('home')

#for register
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

# display record

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,"record.html",{"customer_record":customer_record})
    else:
        messages.success(request,"you must login for see the recordes")
        return redirect('home')

#delete record

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it =Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"record deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"you must login for delete recordes")
        return redirect('home')

# insert record:
def add_record(request):
    form = AddRecordForm((request.POST) or (None))
    if request.user.is_authenticated:
        if request.method =='POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"record added....successfully")
                return redirect('home')
        return render(request,"add_record.html",{'form':form})
    else:
        messages.success(request,"you must be loggedin....")
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"record updated....successfully")
            return redirect('home')
        return render(request,"update_record.html",{'form':form})    
    else:
        messages.success(request,"you must be loggedin....")
        return redirect('home')    
            

