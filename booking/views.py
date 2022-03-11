from django.shortcuts import render
from .forms import AppointmentForm

# Create your views here.


def make_appointment(request):
    """
    Return Make Appointment form rendered in new page
    """
    appointment_form = AppointmentForm()
    return render(request,
                  'make-appointment.html',
                  {'appointment_form': appointment_form})
