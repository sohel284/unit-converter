from django.contrib import admin
from unitconverterapp.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Conversion)
