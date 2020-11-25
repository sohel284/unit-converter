from django.shortcuts import render
from unitconverterapp.models import *


def home(request):
    
    measurements = Measurement.objects.all()
    types = UnitConvertType.objects.all()
    units = UnitType.objects.all()
   
   
    return render(request, 'home.html', {'measurements':measurements, 'types':types, 'units':units})


def measurement_view(request):
    measurement_id = request.GET.get('measurement')
    measurement = None
    
    if measurement_id is not None:
        try:
            measurement = Measurement.objects.get(pk=measurement_id)
        except Measurement.DoesNotExist:
            pass

    measurement = MeasurementArticle.objects.filter(measurement=measurement).get(measurement_id=measurement_id)
    measurements = Measurement.objects.all()
    
    return render(request, 'measurements_article.html', {'measurement':measurement, 'measurements':measurements, })   


def unit_view(request):
    unit_type_id = request.GET.get('unit_type')
    unit_type = None
    if unit_type_id is not None:
        try:
            unit_type = UnitType.objects.get(pk=unit_type_id)
        except UnitType.DoesNotExist:
            pass
    unit_type = UnitArticle.objects.filter(unit_type=unit_type).get(unit_type_id=unit_type_id)

    units = UnitType.objects.all()

    return render(request, 'unit_article.html', {'unit_type':unit_type, 'units':units })        




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
          

    
