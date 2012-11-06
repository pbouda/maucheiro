from django.contrib.gis import admin
from models import Smell

class MyGeoAdmin(admin.options.OSMGeoAdmin):
    default_lon = -964519
    default_lat = 4788370
    default_zoom = 14

admin.site.register(Smell, MyGeoAdmin)