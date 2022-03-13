from django.shortcuts import render
from .forms import AppointmentForm

# Create your views here.


def make_appointment(request):
    """
    Return Make Appointment form rendered in new page
    """
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.save()

    appointment_form = AppointmentForm()
    return render(request,
                  'make-appointment.html',
                  {'appointment_form': appointment_form})
