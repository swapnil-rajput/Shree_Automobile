from django.db import models

# Create your models here.


class product(models.Model):

    name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

