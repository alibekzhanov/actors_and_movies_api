from django.db import models


class Actor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title

