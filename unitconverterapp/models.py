from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)
    symbol_name = models.CharField(max_length=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    wiki_link = models.URLField()

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