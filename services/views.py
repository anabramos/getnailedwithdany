from django.shortcuts import render
from django.views import generic
from .models import Service

# Create your views here.


def get_services(request):
    """
    Renders services page
    """
    services = Service.objects.all()
    context = {
        'services' : services
    }

    return render(request, 'services.html', context)