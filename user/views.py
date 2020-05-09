from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if(request.method=="POST"):
        username = request.POST.get("username");
        password = request.POST.get("password");

        user = authenticate(request,username=username, password=password)

        if(user is not None):
            login(request,user)
            return redirect("recipe_detail.html")
        else:
            messages.info(request,"Invalid username or password")

    return render(request, "user/login.html",{})

def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserCreationForm()
    if(request.method=="POST"):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("login")
    context={
        "form":form
    }
    return render(request, "user/register.html",context)

def user_logout(request):
    logout(request)
    return redirect("login")