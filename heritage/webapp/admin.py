from django.contrib import admin

from .models import *

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Card)
admin.site.register(Image)
admin.site.register(Publication)
admin.site.register(Region)
admin.site.register(Tag)