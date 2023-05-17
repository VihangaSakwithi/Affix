from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['name', 'zip', 'service', 'phone', 'email', 'message']
