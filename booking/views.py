from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import AppointmentForm
from .models import Appointment

# Create your views here.


def make_appointment(request):
    """
    Make new appointment form and post to database
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


def my_account(request):
    """
    Return My Account page to User
    """
    current_user = request.user
    my_appointments = Appointment.objects.filter(user=current_user)
    return render(request, 'my-account.html', {'my_appointments': my_appointments})


def change_appointment(request, appointment_appointment_id):
    """
    Change Appointment details
    """
    appointment = get_object_or_404(Appointment,
                                    appointment_id=appointment_appointment_id)
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST, instance=appointment)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.save()

    appointment_form = AppointmentForm(instance=appointment)
    return render(request, 'change-appointment.html',
                  {'appointment_form': appointment_form})
