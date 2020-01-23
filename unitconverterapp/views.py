from django.shortcuts import render
from unitconverterapp.models import *


# Create your views here.
def home(request, converter_name=None):
    if converter_name is not None:
        try:
            converter = Conversion.objects.select_related('from_unit', 'to_unit').get(name=converter_name)
        except Conversion.DoesNotExist:
            converter = Conversion.objects.first()
    else:
        converter = Conversion.objects.first()
    
    categories = Category.objects.all()
    
    if converter is not None:
        converter.inverse_rate = (1.0 / converter.rate);
        converters = Conversion.objects.filter(
            from_unit__category=converter.from_unit.category
        ).exclude(pk=converter.pk)
    else:
        converters = None

    return render(request, 'home.html', {
        'categories': categories, 
        'converters': converters,
        'conversion': converter
    })