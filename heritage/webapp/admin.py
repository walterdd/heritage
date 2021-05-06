from django.contrib import admin

from .models import Text, Tag, Image

admin.site.register(Text)
admin.site.register(Tag)
admin.site.register(Image)