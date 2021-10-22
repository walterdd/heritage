from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
  image = models.ImageField()


class Author(models.Model):
  name = models.CharField(max_length=200, primary_key=True)


class PeopleGenre(models.Model):
  """Genre of the cards about people."""
  # Human-readable tag.
  name = models.CharField(max_length=200, primary_key=True)


class NoteGenre(models.Model):
  """Genre of the cards of Notes format."""
  # Human-readable tag.
  name = models.CharField(max_length=200, primary_key=True)


class Region(models.Model):
  """Defines region coordinates that corresponds to an area displayed on the map.

  Each region may have many pins - itinerary checkpoints.
  """
  # TODO: define the format for storing map coordinates.
  pass


class Category(models.Model):
  """Category is a common theme of the cards of different formats.

  Defined on the card level."""
  title = models.CharField(max_length=200)
  cover_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)


class StyleTag(models.Model):
  """Tag defining architectural style of an monument on a card.

  Defined only for cards about monuments."""
  name = models.CharField(max_length=200, primary_key=True)


class TimeTag(models.Model):
  """Tag defining construction time of the monument on a card.

  Defined only for cards about monuments."""
  name = models.CharField(max_length=200, primary_key=True)


class RegionTag(models.Model):
  """Tag defining a region where an monument on a card is located.

  Defined only for cards about monuments."""
  name = models.CharField(max_length=200, primary_key=True)
  region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)


class FunctionTag(models.Model):
  """Tag defining a function of the monument on a card.

  Defined only for cards about monuments."""
  name = models.CharField(max_length=200, primary_key=True)


class PinLocation(models.Model):
  """Defines coordinate of the pin, corresponding to a itinerary section."""
  # TODO: define the format for storing map coordinates for pins.
  region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)


class ItineraryStepTag(models.Model):
  """Itinerary section tag, e.g. summer, winter, spring etc."""
  name = models.CharField(max_length=200)


class ItineraryStep(models.Model):
  """Represents one place of interest on the itinerary and an article about it."""
  title = models.CharField(max_length=400)
  tag = models.ManyToManyField(ItineraryStepTag)
  text = models.TextField()
  images = models.ManyToManyField(Image)
  location = models.ForeignKey(PinLocation, on_delete=models.SET_NULL, null=True)
  # The order of this step in the whole itinerary.
  order = models.IntegerField()


class Itinerary(models.Model):
  """Itinerary is a format that represents a collection of points of interest
   conceptually grouped together."""
  title = models.CharField(max_length=200)
  region_tag = models.ForeignKey(RegionTag, on_delete=models.SET_NULL, null=True)
  itinerary_sections = models.ManyToManyField(ItineraryStep)


class Person(models.Model):
  """Person is a format that represents an article about a person."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400, default="")
  text = models.TextField()
  genre = models.ForeignKey(PeopleGenre, on_delete=models.SET_NULL, null=True,  blank=True)
  images = models.ManyToManyField(Image)


class Note(models.Model):
  """Note is a format that represents an article about miscellaneous topics."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400, default="")
  text = models.TextField()
  genre = models.ForeignKey(NoteGenre, on_delete=models.SET_NULL, null=True,  blank=True)
  images = models.ManyToManyField(Image)


class Monument(models.Model):
  """Monument is a format that represents an article about a monument."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400, default="")
  text = models.TextField()
  images = models.ManyToManyField(Image, blank=True)
  style_tag = models.ForeignKey(StyleTag, on_delete=models.SET_NULL, null=True,  blank=True)
  time_tag = models.ForeignKey(TimeTag, on_delete=models.SET_NULL, null=True,  blank=True)
  region_tag = models.ForeignKey(RegionTag, on_delete=models.SET_NULL, null=True,  blank=True)
  function_tag = models.ForeignKey(FunctionTag, on_delete=models.SET_NULL, null=True,  blank=True)
  # Itineraries that included a monument from the card.
  related_itineraries = models.ManyToManyField(Itinerary, blank=True)


class Card(models.Model):
  """Card represents a unit of content of different formats.

  Card stores all the required information to display an icon for this
  content unit. The link to the content itself is stored as a foreign key to the
  objects of different formats, such as Person, Note, Monument and Itinerary."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400, blank=True)
  cover_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
  authors = models.ManyToManyField(Author, blank=True)
  publication_date = models.DateTimeField(auto_now_add=True)
  # Card can either contain one of: a person, a note, a monument or an itinerary.
  # Content defines the format.
  person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True,  blank=True)
  note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True,  blank=True)
  monument = models.ForeignKey(Monument, on_delete=models.SET_NULL, null=True,  blank=True)
  itinerary = models.ForeignKey(Itinerary, on_delete=models.SET_NULL, null=True,  blank=True)

  # Formats corresponding to the sections of the site.
  # Each text will be attributed to one of those categories.
  class Format(models.TextChoices):
    ITINERARIES = 'ITINERARIES', _('МАРШРУТЫ')
    NOTES = 'NOTES', _('ЗАМЕТКИ')
    PEOPLE = 'PEOPLE', _('ЛЮДИ')
    CARDS = 'CARDS', _('КАРТОТЕКА')

  format = models.CharField(
      max_length=20,
      choices=Format.choices,
  )

  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,  blank=True)


class Publication(models.Model):
  """Cards grouped by a common theme.

  Same as 'vypusk'."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400, default='')
  image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
  cards = models.ManyToManyField(Card)
  publication_date = models.DateTimeField(auto_now_add=True)





