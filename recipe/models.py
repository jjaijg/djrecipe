from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    name        = models.CharField(max_length=20)
    cuisine     = models.TextField(blank=True, null =True)  #description
    time_hours = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(24),
            MinValueValidator(0)
        ]
    )
    time_min = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0)
        ]
    )
    ingredients = models.TextField()
    method      = models.TextField(default='Recipe method!')
    author      = models.ForeignKey(User,default=None,null = True,on_delete=models.CASCADE)