from django.db import models

# Create your models here.


class Laptop(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    cat = models.CharField(max_length=50)
    cmp = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
