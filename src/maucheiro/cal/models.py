#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Smell(models.Model):
    date_start = models.DateTimeField("Start date of smell")
    date_end = models.DateTimeField("End date of smell")

    geometry = models.PointField("Location of smell", srid=4326)

    objects = models.GeoManager()

    def __unicode__(self):
        return '%s - %s: %s %s' % (self.date_start, self.date_end, self.geometry.x, self.geometry.y)