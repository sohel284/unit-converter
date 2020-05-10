from django.contrib import admin
from unitconverterapp.models import *

# Register your models here.

class ConversionAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_unit', 'to_unit', 'rate', )
    list_select_related = ('from_unit', 'to_unit',)
    

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Conversion, ConversionAdmin)
