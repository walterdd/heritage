from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = '__all__'

class PeopleGenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = PeopleGenre
    fields = ['name']

class NoteGenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = NoteGenre
    fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
  cover_image = ImageSerializer(read_only=True)

  class Meta:
    model = Category
    fields = ['title', 'cover_image']

class CardSerializer(serializers.ModelSerializer):
  cover_image = ImageSerializer(read_only=True)
  authors = AuthorSerializer(many=True, read_only=True)
  cover_image = ImageSerializer(read_only=True)
  category = CategorySerializer(read_only=True)

  class Meta:
    model = Card
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

class PublicationSerializer(serializers.ModelSerializer):
  image = ImageSerializer(read_only=True)
  cards = CardSerializer(many=True, read_only=True)

  class Meta:
    model = Publication
    fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
  genre = PeopleGenreSerializer(read_only=True)
  images = ImageSerializer(many=True, read_only=True)

  class Meta:
    model = Person
    fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
  genre = NoteGenreSerializer(read_only=True)
  images = ImageSerializer(many=True, read_only=True)

  class Meta:
    model = Person
    fields = '__all__'