from django.db import models
from django.urls import reverse
from services.models import Services

# Creating a Customers model
class Customers(models.Model):
    name    = models.CharField(max_length=100, default=None)
    email   = models.EmailField(max_length=100, default=None)
    cell    = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customers:customer_update', kwargs={'pk': self.pk})

# Creating a CustomersPrice model
class CustomersPrice(models.Model):
    services    = models.ForeignKey(Services, on_delete=models.CASCADE)
    price       = models.IntegerField(default=None)
    customer_id = models.IntegerField(default=None, null=True)
    staff_id    = models.IntegerField(default=None, null=True)

    def __str__(self):
        return self.price

    def get_absolute_url(self):
        return reverse('customers:customer_update', kwargs={'pk': self.pk})
