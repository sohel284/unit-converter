from django.shortcuts import render
from unitconverterapp.models import *


def home(request):
    
    
    return render(request, 'home.html', {
        
        
    })




def unitconvert(request, converter_name=None):
    unit_convert_type_id = request.GET.get('unit_convert_type')
    
    converter = None
    unit_convert_type = None

    if converter_name is not None:
        try:
            converter = Conversion.objects.select_related('from_unit', 'from_unit__unit_convert_type', 'to_unit').get(name=converter_name)
        except Conversion.DoesNotExist:
            pass
    if unit_convert_type_id is not None:
        try:
            unit_convert_type = UnitConvertType.objects.get(pk=unit_convert_type_id)
        except UnitConvertType.DoesNotExist:
            pass


    if converter is None:
        converter = Conversion.objects.select_related('from_unit', 'from_unit__unit_convert_type', 'to_unit')
        if unit_convert_type is not None:
            converter = converter.filter(from_unit__unit_convert_type=unit_convert_type)
        converter = converter.first()
    
    types = UnitConvertType.objects.all()
    
    if converter is not None:
        converter.inverse_rate = (1.0 / converter.rate);
        converters = Conversion.objects.filter(
            from_unit__unit_convert_type=converter.from_unit.unit_convert_type
        ).exclude(pk=converter.pk)
    else:
        converters = None
    
    
       
    return  render(request, 'unit_convert_page.html', { 

        'types': types,
        'converters': converters,
        'conversion': converter,
        

        })         

    
def lengthview(request):
    return render(request, 'measurements/length.html', )
def weightview(request):
    return render(request, 'measurements/weight.html', )    
        