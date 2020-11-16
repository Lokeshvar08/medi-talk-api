from django.db import models


# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=250)
    specialisation = models.CharField(max_length=250)
    hospital = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    application_rating = models.FloatField()
    google_rating = models.FloatField()
    article_rating = models.FloatField()
    average_rating = models.FloatField()

    def __str__(self):
        return self.name


"""
    {
    "name":"Lokeshvar",
    "specialisation":"dentist",
    "hospital": "Government Hospital",
    "location": "coimbatore",
    "application_rating":4.0,
    "google_rating": 3.8,
    "article_rating": 4.2,
    "average_rating": 4.0
    }
"""
