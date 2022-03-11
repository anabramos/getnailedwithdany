from django.db import models
from django.contrib.auth.models import User
from services.models import Service

time_options = (
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
)

status_options = (
    ("pending", "pending"),
    ("confirmed", "confirmed"),
    ("denied", "denied"),
)

# Create your models here.


class Customer(models.Model):
    """
    Model for customer details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    """
    Model for making appointment requests
    """
    appointment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=10,
                                        choices=time_options,
                                        default='00:00')
    status = models.CharField(max_length=50,
                              choices=status_options,
                              default="pending")

    class Meta:
        """
        Order appointments by date
        """
        ordering = ['appointment_date']

    def __str__(self):
        return str(self.appointment_id)
