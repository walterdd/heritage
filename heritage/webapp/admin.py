from django.contrib import admin
from .models import *

class ImageAdmin(admin.ModelAdmin): # new
   readonly_fields = ('img_preview',)
   list_display = ('id', 'img_preview',)

   def img_preview(self, obj):
           return obj.img_preview

   img_preview.short_description = 'Image Preview'
   img_preview.allow_tags = True

class CardAdmin(admin.ModelAdmin): # new
   readonly_fields = ('img_preview',)
   list_display = ('__str__', 'category', 'publication_date', 'img_preview',)

   def img_preview(self, obj):
           return obj.img_preview

   img_preview.short_description = 'Image Preview'
   img_preview.allow_tags = True

class PublicationAdmin(admin.ModelAdmin): # new
   readonly_fields = ('img_preview',)
   list_display = ('__str__', 'publication_date', 'img_preview',)

   def img_preview(self, obj):
           return obj.img_preview

   img_preview.short_description = 'Image Preview'
   img_preview.allow_tags = True

admin.site.register(Author)
admin.site.register(Card, CardAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Article)
