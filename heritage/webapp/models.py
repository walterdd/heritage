from django.db import models
from django.utils.translation import gettext_lazy as _


class TextTag(models.Model):
  """Tag that defines a genre of the text."""
  # Human-readable tag.
  name = models.CharField(max_length=200, primary_key=True)

class Region(models.Model):
  """Defines region coordinates that corresponds to an area displayed on the map.

  Each region may have many pins - itinerary checkpoints.
  """
  # TODO: define the format for storing map coordinates.
  pass

class StyleTag(models.Model):
  """Tag defining architectural style of an monument on a card."""
  name = models.CharField(max_length=200, primary_key=True)

class TimeTag(models.Model):
  """Tag defining construction time of the monument on a card."""
  name = models.CharField(max_length=200, primary_key=True)

class RegionTag(models.Model):
  """Tag defining a region where an monument on a card is located."""
  name = models.CharField(max_length=200, primary_key=True)
  region = models.ForeignKey(Region, on_delete=models.CASCADE)

class FunctionTag(models.Model):
  """Tag defining a function of the monument on a card."""
  name = models.CharField(max_length=200, primary_key=True)

class Image(models.Model):
  image = models.ImageField()

class Text(models.Model):
  # Categories corresponding to the sections of the site.
  # Each text will be attributed to one of those categories.
  class Category(models.TextChoices):
    ITINERARIES = 'ITINERARIES', _('МАРШРУТЫ')
    NOTES = 'NOTES', _('ЗАМЕТКИ')
    PEOPLE = 'PEOPLE', _('ЛЮДИ')
    CARDS = 'CARDS', _('КАРТОТЕКА')

  title = models.CharField(max_length=200)
  text = models.TextField()
  author = models.CharField(max_length=30)
  tag = models.ForeignKey(TextTag, on_delete=models.CASCADE)
  images = models.ManyToManyField(Image)
  publication_date = models.DateTimeField(auto_now_add=True)
  category = models.CharField(
      max_length=20,
      choices=Category.choices,
  )

class PinLocation(models.Model):
  """Defines coordinate of the pin, corresponding to a itinerary section."""
  # TODO: define the format for storing map coordinates for pins.
  region = models.ForeignKey(Region, on_delete=models.CASCADE)


class ItineraryStepTag(models.Model):
  """Itinerary section tag, e.g. summer, winter, spring etc."""
  name = models.CharField(max_length=200)


class ItineraryStep(models.Model):
  """Defines an itinerary steps and stores all the information about this step."""
  title = models.CharField(max_length=400)
  tag = models.ManyToManyField(ItineraryStepTag)
  text = models.TextField()
  images = models.ManyToManyField(Image)
  location = models.ForeignKey(PinLocation, on_delete=models.CASCADE)


class Itinerary(models.Model):
  """Itinerary is a sequence of ItinerarySteps."""
  title = models.CharField(max_length=200)
  # Image that will be set on the Itinerary icon.
  cover_image = models.ForeignKey(Image, on_delete=models.CASCADE)
  region_tag = models.ForeignKey(RegionTag, on_delete=models.CASCADE)
  # NOTE: A tricky part will be to display ItineraryStep in the right order.
  itinerary_sections = models.ManyToManyField(ItineraryStep)


class Card(models.Model):
  """Card represents a page about a monument that was featured in either a text
   or an itinerary, that deserves to be added to the card library."""
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=400)
  cover_image = models.ForeignKey(Image, on_delete=models.CASCADE)
  style_tag = models.ForeignKey(StyleTag, on_delete=models.CASCADE)
  time_tag = models.ForeignKey(TimeTag, on_delete=models.CASCADE)
  region_tag = models.ForeignKey(RegionTag, on_delete=models.CASCADE)
  function_tag = models.ForeignKey(FunctionTag, on_delete=models.CASCADE)
  # images = models.ManyToManyField(Image)
  text = models.TextField()
  # Itineraries that included a monument from the card.
  related_itineraries = models.ManyToManyField(Itinerary)
  # Texts that mentioned the monument.
  related_texts = models.ManyToManyField(Text)


class Collection(models.Model):
  """In other words, a pool. A collection of texts and itineraries grouped by
  a certain topic. Collection typically contains 2 texts and an itinerary"""
  title = models.CharField(max_length=200)
  texts = models.ManyToManyField(Text)
  itineraries = models.ManyToManyField(Itinerary)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)
  publication_date = models.DateTimeField(auto_now_add=True)


class Publication(models.Model):
  """Itinerary and texts grouped by a common theme."""
  title = models.CharField(max_length=200)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)
  texts = models.ManyToManyField(Text)
  itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
  publication_date = models.DateTimeField(auto_now_add=True)



