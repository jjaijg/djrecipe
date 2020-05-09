from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):  #kwargs=>keyword args
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):  #kwargs=>keyword args
    return render(request,"contact.html",{})

def about_view(request, *args, **kwargs):  #kwargs=>keyword args
    my_context={
        "my_name" : "Niki",
        "my_number" :123,
        "my_list":[123,12344,12343]
    }
    return render(request,"about.html",my_context)

def social_view(request, *args, **kwargs):  #kwargs=>keyword args
    return HttpResponse("<h1>Social Page</h1>")