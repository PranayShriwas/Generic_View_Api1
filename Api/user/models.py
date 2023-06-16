from django.db import models

# Create your models here.


class user(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=50)
    Address = models.TextField()

    def __str__(self) -> str:
        return self.Username
