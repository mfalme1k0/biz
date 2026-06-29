from django.shortcuts import render

# Create your views here.
def home(request):
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