from django.contrib import admin
from webApp.models import product, customer, vehicle

# Register your models here.

admin.site.register(product)
admin.site.register(customer)
admin.site.register(vehicle)