from django.db import models


# Create your models here.
class Country(models.Model):
    state = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.state

