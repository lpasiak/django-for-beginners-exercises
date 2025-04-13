from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def home_page_view(request):
    return HttpResponse(f"Secret key is loaded: {(settings.SECRET_KEY)}")