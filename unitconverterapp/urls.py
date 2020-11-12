from django.urls import path, include
from unitconverterapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:converter_name>', views.home, name='converter'),

    path('test/', views.mytest , name='mytest'),
    path('length/', views.lengthview, name='lengthview'),
    path('weight/', views.weightview, name='weightview'),


]
