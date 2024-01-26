from django.db import models

# Create your models here.
class Musician(models.Model):
    INSTRUMENTS = [
        ('GUITAR', 'Guitar'),
        ('PIANO', 'Piano'),
        ('DRUM', 'Drum'),
        ('KEYBOARD', 'Keyboard'),
        ('VIOLIN', 'Violin'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    instrument_type = models.CharField(
        max_length=50,
        choices=INSTRUMENTS,
        default='Guitar'
    )
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'