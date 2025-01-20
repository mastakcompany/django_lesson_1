from django.db import models


class Coordinate(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    
    def __str__(self):
        return f'{self.lat}:{self.lon}'
    
    class Meta:
        ordering = ['lat', 'lon']


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.OneToOneField(Coordinate, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


