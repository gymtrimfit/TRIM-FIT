from django.shortcuts import render

# Create your views here.
def index(request):
    print("hiiii")
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def gallery(request):
    return render(request,'gallery.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def typography(request):
    return render(request,'typography.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def GYMREGISTER(request):
    return render(request,'GYMREGISTER.html')