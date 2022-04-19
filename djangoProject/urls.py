from django.contrib import admin
from django.urls import path
from PoliceProject.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name='Home'),
]