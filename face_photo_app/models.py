import os
from django.db import models

# Create your models here.
class CustomUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    organizationname = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.phone

class AddNewCustomer(models.Model):
    Customer_full_name = models.CharField(max_length=25)
    Organization_name = models.CharField(max_length=30, blank=True, null=True)
    Customer_email = models.EmailField(max_length=254)
    Customer_mobile = models.CharField(max_length=15, unique=True)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.Customer_full_name

class Event(models.Model):
    admin = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    customer = models.ForeignKey(AddNewCustomer, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

def get_admin_event_upload_path(instance, filename):
    admin_username = instance.event.admin.username
    customer_name = instance.event.customer.Customer_full_name
    event_name = instance.event.name
    return os.path.join(admin_username, customer_name, event_name, filename)

def get_admin_background_upload_path(instance, filename):
    admin_username = instance.event.admin.username
    customer_name = instance.event.customer.Customer_full_name
    event_name = instance.event.name
    return os.path.join(admin_username, customer_name, event_name, filename)

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_admin_event_upload_path)
    bg_image = models.ImageField(upload_to=get_admin_background_upload_path, null=True)

    def __str__(self):
        return self.image.name


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name