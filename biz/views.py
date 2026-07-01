from django.shortcuts import render
from biz.models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        mycontact = Contact(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                subject=request.POST.get('subject'),
                message=request.POST.get('message')
                )
        mycontact.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'services-details.html')

def starterpage(request):
    return render(request, 'starter-page.html')