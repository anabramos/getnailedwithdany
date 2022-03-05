from django.shortcuts import render


# Create your views here.

def homepage(request):
    # Return homepage
    return render(request, 'homepage.html')
