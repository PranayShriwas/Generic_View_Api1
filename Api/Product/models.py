from django.db import models

# Create your models here.


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    Cat = models.CharField(max_length=50)
    Cmp = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Name
