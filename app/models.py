from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
