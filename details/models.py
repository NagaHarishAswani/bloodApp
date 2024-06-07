from django.db import models

class DonorModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    bg = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    phno = models.CharField(max_length=50)

class Meta:
    model=DonorModel
    ordering=('name',)
