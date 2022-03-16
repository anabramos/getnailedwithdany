from django.db import models


# Create your models here.

class Service(models.Model):
    """
    Model for each service provided
    """
    service_id = models.AutoField(primary_key=True)
    service_title = models.CharField(max_length=50, unique=True)
    service_description = models.CharField(max_length=200, unique=True)
    service_price = models.FloatField()

    class Meta:
        """
        Order Services by title
        """
        ordering = ['service_title']

    def __str__(self):
        return str(self.service_title)
