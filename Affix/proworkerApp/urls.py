from django.urls import path, re_path
from proworkerApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('proworkers', views.proworkerApi),
    path('proworkers/savefile', views.SaveFile)
]