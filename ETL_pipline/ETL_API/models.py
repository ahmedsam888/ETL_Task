from django.db import models

class car_data(models.Model):

    #id = models.IntegerField(primary_key=True)
    car_model = models.CharField(max_length=100)
    year_of_manufacture = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    age = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'car_data'