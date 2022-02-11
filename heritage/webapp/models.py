from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class Image(models.Model):
  image = models.ImageField()


class Author(models.Model):
  name = models.CharField(max_length=200, primary_key=True)


class Tag(models.Model):
  """Tags define different taxonomies of articles.

  It can define different taxonomies, such as a genre, a reqion of Russia or a
  location, or a topic. Tag taxonomy is defined by the type field."""
  name = models.CharField(max_length=200, primary_key=True)
  type = models.CharField(max_length=200, blank=False)

  class Meta:
    unique_together = (("name", "type"),)


class Card(models.Model):
  """Card represents a unit of content of different formats.

  Card stores all the required information to display an icon for this
  content unit. The link to the content itself is stored as a foreign key to the
  objects of different formats, such as Person, Note, Monument and Itinerary."""

  class Category(models.TextChoices):
    """Category define the highest-level taxonomy of articles.
    It determines the sections of the site."""
    ITINERARY = 'ITINERARY', _('МАРШРУТ')
    NOTE = 'NOTE', _('ЗАМЕТКА')
    PEOPLE = 'PEOPLE', _('ЛЮДИ')
    MONUMENT = 'MONUMENT', _('ПАМЯТНИК')

  title = models.CharField(max_length=200, blank=False)
  subtitle = models.CharField(max_length=400, blank=True)
  category = models.CharField(
      max_length=20,
      choices=Category.choices,
  )
  cover_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True,
                                  blank=True)
  authors = models.ManyToManyField(Author, blank=True)
  publication_date = models.DateTimeField(auto_now_add=True)
  tags = models.ManyToManyField(Tag)


class Article(models.Model):
  """Article represents a unique material."""
  text = RichTextUploadingField()
  images = models.ManyToManyField(Image)
  card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=False,
                           related_name="article")


class Publication(models.Model):
  """Cards grouped by a common theme.

  Can contain multiple articles and an itinerary."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400, default='')
  cover_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
  cards = models.ManyToManyField(Card)
  publication_date = models.DateTimeField(auto_now_add=True)


class Region(models.Model):
  """Defines region coordinates that corresponds to an area displayed on the map.

  Each region may have many pins - itinerary checkpoints.
  """
  # TODO: define the format for storing map coordinates.
  name = models.CharField(max_length=200, primary_key=True)