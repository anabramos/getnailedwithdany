from django.contrib import admin
from .models import Appointment, Service

# Register your models here.


@admin.register(Appointment)
class AppointmentAdmim(admin.ModelAdmin):
    """ Customize admin view of appointments in the back end with such fields """
    list_filter = ('timestamp', 'status')
    list_display = ('timestamp', 'service', 'status','user', 'appointment_id')

