from django.shortcuts import render
from .forms import ContactUsForm


# Create your views here.

def homepage(request):
    # Return homepage
    return render(request, 'homepage.html')
