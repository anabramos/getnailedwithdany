from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    """
    Creates Form from Appointment Module
    """
    class Meta:
        """
        Renders specific fields from the Appointment Module into the Form
        """
        model = Appointment
        fields = ['service',
                  'appointment_date',
                  'appointment_time']
