from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)


class Unit(models.Model):
    name = models.CharField(max_length=20)
    symbol_name = models.CharField(max_length=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    wiki_link = models.URLField()


class Conversion(models.Model):
    from_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='')
    to_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    rate = models.FloatField()