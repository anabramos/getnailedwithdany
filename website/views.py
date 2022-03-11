from django.shortcuts import render
from .forms import ContactUsForm


# Create your views here.

def homepage(request):
    """
    Return homepage
    """
    return render(request, 'homepage.html')


def contact_us(request):
    """
    Return Contact Us form rendered in a new page
    """
    contact_form = ContactUsForm()
    return render(request, 'contact-us.html', {'contact_form': contact_form})

def my_account(request):
    """
    Return My Account page to User
    """
    return render(request, 'my-account.html')
