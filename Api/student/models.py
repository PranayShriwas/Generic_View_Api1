from django.db import models

# Create your models here.


class Student(models.Model):
    Stu_Reg = models.CharField(max_length=50)
    Stu_Name = models.CharField(max_length=50)
    Stu_email = models.EmailField(max_length=254)
    Stu_password = models.CharField(max_length=50)
    Stu_Number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Stu_Name
