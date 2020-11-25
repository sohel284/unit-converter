from django.db import models

# Create your models here.

class Measurement(models.Model):
    name = models.CharField(max_length=50, )
    
    def __str__(self):
        return self.name

class UnitType(models.Model):
    name = models.CharField(max_length=50,  )
    
    def __str__(self):
        return self.name      

class MeasurementArticle(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measurement_name')
    measurement_description = models.TextField()
    measurement_title = models.CharField(max_length=100, null=True, blank=True)
    measurement_article_link = models.URLField(null=True, blank=True)
    measurement_img = models.ImageField(upload_to="measurement", blank=True, null=True)

    def __str__(self):
        return self.measurement_title

class UnitArticle(models.Model):
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE, related_name='unit_name', null=True)
    unit_description = models.TextField()
    unit_title = models.CharField(max_length=100, null=True, blank=True)
    unit_article_link = models.URLField(null=True, blank=True)
    unit_img = models.ImageField(upload_to="unit" , blank=True, null=True,)

    def __str__(self):
        return self.unit_title




class UnitConvertType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)
    symbol_name = models.CharField(max_length=5)
    unit_convert_type = models.ForeignKey(UnitConvertType, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000, null=True, blank=True)
   
    def __str__(self):
        return "%s (%s)" % (self.name, self.symbol_name)





class Conversion(models.Model):
    from_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='from_conversions')
    to_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='to_conversions')
    rate = models.FloatField()
    name = models.SlugField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_unit', 'to_unit'], name='uniq_from_to_units'),
            models.UniqueConstraint(fields=['name'], name='uniq_converter_name')
        ]