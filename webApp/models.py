from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


class customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    address = models.CharField(max_length=100,blank=True)
    mobile_no = models.IntegerField(blank=True)


class vehicle(models.Model):
    type = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    owner = models.CharField(max_length=100)
