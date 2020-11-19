from django.urls import path, include
from unitconverterapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('convert', views.unitconvert, name='unitconvert'),
    path('<slug:converter_name>', views.unitconvert, name='converter'),


    
    path('length/', views.lengthview, name='lengthview'),
    path('weight/', views.weightview, name='weightview'),


]
