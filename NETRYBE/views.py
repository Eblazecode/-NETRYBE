from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "fitzzy/index.html" , {})

def about(request):
    return render(request,"fitzzy/about.html",{})

def training(request):
        return render(request, "fitzzy/courses.html",{})

def coursesdet(request):
    return render(request, "fitzzy/coursesdetails.html",{})

def datasci(request):
    return render(request, "fitzzy/datasci.html",{})

def frontend(request):
    return render(request, "fitzzy/frontend.html",{})

def productdesign(request):
    return render(request,"fitzzy/uiux.html", {})


def contact(request):
    return render(request,"fitzzy/contact.html", {})

def backend(request):
    return render(request,"fitzzy/backend.html", {})
def schprog(request):
    return render(request, "fitzzy/schprog.html", {})
