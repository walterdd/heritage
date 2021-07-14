from django.contrib import admin

from .models import *

admin.site.register(Text)
admin.site.register(TextTag)
admin.site.register(Region)
admin.site.register(RegionTag)
admin.site.register(TimeTag)
admin.site.register(StyleTag)
admin.site.register(FunctionTag)
admin.site.register(ItineraryStepTag)
admin.site.register(Itinerary)
admin.site.register(ItineraryStep)
admin.site.register(Card)
admin.site.register(Collection)
admin.site.register(Publication)
admin.site.register(PinLocation)
admin.site.register(Image)
