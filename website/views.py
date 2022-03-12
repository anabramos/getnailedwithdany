from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
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
    # submitted = False
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():

            # Stores form data in variable as dictionary
            message_data = contact_form.cleaned_data

            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(message_data['subject'],
                      message_data['message'],
                      message_data['email'],
                      recipient_list)
  
            return HttpResponseRedirect('/contact-us')
    else:
        contact_form = ContactUsForm()

    return render(request, 'contact-us.html', {'contact_form': contact_form})


def my_account(request):
    """
    Return My Account page to User
    """
    return render(request, 'my-account.html')
