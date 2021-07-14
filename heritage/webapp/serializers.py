from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = '__all__'

class TextTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = TextTag
    fields = ['name']

class TextSerializer(serializers.ModelSerializer):
  tag = TextTagSerializer(read_only=True)
  images = ImageSerializer(many=True, read_only=True)

  class Meta:
    model = Text
    fields = '__all__'

class StyleTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = StyleTag
    fields = ['name']

class TimeTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeTag
    fields = ['name']

class FunctionTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = FunctionTag
    fields = ['name']

class RegionTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = RegionTag
    fields = ['name', 'region']

class ItinerarySerializer(serializers.ModelSerializer):
  cover_image = ImageSerializer(read_only=True)

  class Meta:
    model = Itinerary
    fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
  texts = TextSerializer(many=True, read_only=True)
  itineraries = ItinerarySerializer(many=True, read_only=True)
  image = ImageSerializer(read_only=True)

  class Meta:
    model = Collection
    fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
  image = ImageSerializer(read_only=True)
  texts = TextSerializer(many=True, read_only=True)
  itinerary = ItinerarySerializer(read_only=True)

  class Meta:
      model = Publication
      fields = '__all__'