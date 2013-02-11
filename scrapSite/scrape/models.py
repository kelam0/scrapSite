from django.db import models

# Create your models here.
class scraper(models.Model):
    spot_date = models.DateField()               #TEXT
    hour = models.IntegerField()                 #INT
    weighted_avg = models.FloatField()           #REAL
    
    def __unicode__(self):                       #Print function
        return self.weighted_avg

    def average(self):
        return unicode("average")
