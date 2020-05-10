from django.shortcuts import render
from unitconverterapp.models import *


# Create your views here.
def home(request, converter_name=None):
    category_id = request.GET.get('category')
    
    converter = None
    category = None

    if converter_name is not None:
        try:
            converter = Conversion.objects.select_related('from_unit', 'to_unit').get(name=converter_name)
        except Conversion.DoesNotExist:
            pass
    if category_id is not None:
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            pass


    if converter is None:
        converter = Conversion.objects.select_related('from_unit', 'to_unit')
        if category is not None:
            converter = converter.filter(from_unit__category=category)
        converter = converter.first()
    
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