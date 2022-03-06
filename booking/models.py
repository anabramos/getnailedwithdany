from django.db import models


# Create your models here.

class Customer(models.Model):
    """
    Model for customer details
    """
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=254, default="", unique=True)

    def __str__(self):
        """
        Return customer name
        """
        return self.customer_name
