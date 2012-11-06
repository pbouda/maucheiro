from django.contrib.gis import admin
from models import Smell

admin.site.register(Smell, admin.GeoModelAdmin)