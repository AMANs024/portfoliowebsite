from django.shortcuts import render , redirect
from django.contrib import messages
from portfolio.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('name')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"thank you")
        return redirect('/contact')

        
        
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def resume(request):
    return render(request,'resume.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')