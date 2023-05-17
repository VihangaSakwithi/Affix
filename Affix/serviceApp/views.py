from django.shortcuts import render
from serviceApp.models import Service

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import BookingForm

def showdata(request):
    results = Service.objects.all()
    return render(request, 'index.html',{"data": results})

def bookings_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            zip = form.cleaned_data.get('zip')
            service = form.cleaned_data.get('service')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
