from django.urls import path, re_path
from serviceApp import views

from django.conf.urls.static import static
from django.conf import settings

from .views import bookings_form

urlpatterns = [
    path("", views.showdata),
    path('book/', bookings_form, name='booking_form'),
]