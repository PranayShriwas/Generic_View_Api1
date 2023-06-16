# Generated by Django 4.1.5 on 2023-06-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("FirstName", models.CharField(max_length=50)),
                ("LastName", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=50)),
                ("Address", models.TextField()),
                ("Mobile_no", models.CharField(max_length=50)),
            ],
        ),
    ]
