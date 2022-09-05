from django.db import models

# Create your models here.
class Rocket(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=100, decimal_places=50)
    dateProduced = models.DateTimeField()
    dateLastLaunched = models.DateTimeField()

    def __str__(self):
        return self.name