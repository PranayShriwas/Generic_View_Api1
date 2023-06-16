from django.db import models

# Create your models here.


class Emp(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    Address = models.TextField()
    Mobile_no = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.FirstName
