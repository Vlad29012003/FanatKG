from django.db import models

class Price(models.Model):
    package_name = models.CharField(max_length=100)
    comfort_price = models.DecimalField(max_digits=10, decimal_places=2)
    comfort_plus_price = models.DecimalField(max_digits=10, decimal_places=2)
    beer_price = models.DecimalField(max_digits=10, decimal_places=2)
    exclusive_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.package_name


