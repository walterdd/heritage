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


class CardSerializer(serializers.ModelSerializer):
  cover_image = ImageSerializer(read_only=True)
  authors = AuthorSerializer(many=True, read_only=True)

  class Meta:
    model = Card
    fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['name']


class ArticleSerializer(serializers.ModelSerializer):
  images = ImageSerializer(many=True, read_only=True)
  tags = TagSerializer(many=True, read_only=True)
  card = CardSerializer(many=False, read_only=True)

  class Meta:
    model = Article
    fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
  cover_image = ImageSerializer(many=False, read_only=True)
  cards = CardSerializer(many=True, read_only=True)

  class Meta:
    model = Publication
    fields = '__all__'
