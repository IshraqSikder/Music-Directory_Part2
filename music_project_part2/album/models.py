from django.db import models
from musician.models import Musician
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Album(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    album_name = models.CharField(max_length=20)
    singer = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        default='1'
    )
    
    def __str__(self):
        return self.album_name