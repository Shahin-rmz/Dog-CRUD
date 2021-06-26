from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
from django.db import models

class Dog(models.Model):
    nickname = models.CharField(max_length = 200)
    weight = models.IntegerField()
    food = models.CharField(max_length = 50)
   
    def __str__(self):
        return self.nickname

class Breed(models.Model):
    DogsWithThatName = models.ForeignKey(Dog,models.CASCADE) 
    population = models.IntegerField(MinValueValidator(1))
    tamed = models.BooleanField()

    def __str__(self):
        return self.DogsWithThatName
