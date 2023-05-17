from django.contrib import admin
from .models import Service
from .models import Bookings
# Register your models here.

admin.site.register(Service)
admin.site.register(Bookings)