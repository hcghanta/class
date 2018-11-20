from django.db import models

# Create your models here.

class Currency(models.Model):
    symbol = models.CharField(max_length=3)
    value_convert = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name_plural = 'currencies'
