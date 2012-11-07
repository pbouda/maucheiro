from django.shortcuts import render
import floppyforms as forms
from django.contrib.admin import widgets

from cal.models import Smell

class GMapPointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    map_srid = 900913  # Use the google projection
    template_name = 'google_map.html'

    class Media:
        extend = False
        js = (
            '/static/js/vendor/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
            'http://maps.google.com/maps/api/js?sensor=false',
        )

class GeoForm(forms.Form):
    point = forms.gis.PointField(widget=GMapPointWidget)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()


def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = { "form": GeoForm() }
    return render(request, 'index.html', context)
