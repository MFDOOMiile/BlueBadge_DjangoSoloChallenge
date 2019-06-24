from django.db import models

# Create your models here.
class Player(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    ingame_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    team = models.CharField(max_length=30)
    race = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.fname} {self.lname}'