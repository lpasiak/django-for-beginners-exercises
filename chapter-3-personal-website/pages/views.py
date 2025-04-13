from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse('<h1>Homepage</h1>')

def about_page_view(request):
    context = {'name': 'Łukasz', 'age': 27}

    return render(request, 'pages/about.html', context)
