from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactUsForm


# Create your views here.

def homepage(request):
    """ Return homepage """
    return render(request, 'homepage.html')


def contact_us(request):
    """ Return Contact Us form rendered in a new page """
    # Variable asserts if contact form has been successfully sent
    message_sent = False
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():

            # Stores form data in variable as dictionary
            message_data = contact_form.cleaned_data

            # Send e-mail with form data after validation
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(message_data['subject'],
                      message_data['message'],
                      message_data['email'],
                      recipient_list)

            # Thanks for the tutoring team to helping me with setting up
            # This get request redirect from posting the form
            return HttpResponseRedirect('/contact-us?message_sent=True')
    else:
        contact_form = ContactUsForm()
        if 'message_sent' in request.GET:
            message_sent = True

    return render(request, 'contact-us.html', {'contact_form': contact_form,
                                               'message_sent': message_sent})
