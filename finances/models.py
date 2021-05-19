from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    indicator = models.IntegerField(default=0)

class Credits(models.Model):
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)