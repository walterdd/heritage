from django.contrib import admin

from .models import Text, Tag

admin.site.register(Text)
admin.site.register(Tag)