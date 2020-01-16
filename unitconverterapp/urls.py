from django.urls import path, include
from unitconverterapp import views


urlpatterns = [
    path('', views.home, name='home'),
]
