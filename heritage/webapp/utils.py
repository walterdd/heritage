from .models import *

def get_texts_and_tags_for_category(category, request):
  """Returns a dict with texts and tags corresponding to the category.

  Args:
    request: If request contains tag, the results will be filtered by tag.

  Returns:
    dict with texts, tags found in these texts and category.
  """
  tag_name = request.GET['tag_name'] if request.GET['tag_name'] else None
  if tag_name:
    texts = Text.objects.filter(category__exact=category).filter(tag__exact=tag_name).order_by("publication_date")
    tags = Tag.objects.filter(pk=tag_name)
  else:
    texts = Text.objects.filter(category__exact=category).order_by("publication_date")
    tags_ids = [text.tag for text in texts]
    tags = Tag.objects.filter(pk__in=tags_ids).order_by("name")
  return {"texts" : texts, "tags" : tags, "category" : category}


def get_cards_and_tags_for_category(category, request):
  """Returns a dict with cards and tags of multiple types.

  Args:
    request: If request contains style_tag / function_tag / time_tag / region_tag
      the results will be filtered by tag.

  Returns:
    dict with texts, tags found in these texts and category.
  """
  style_tag_name = request.GET['style_tag_name'] if request.GET['style_tag_name'] else None
  time_tag_name = request.GET['time_tag_name'] if request.GET['time_tag_name'] else None
  function_tag_name = request.GET['function_tag_name'] if request.GET['function_tag_name'] else None
  region_tag_name = request.GET['region_tag_name'] if request.GET['region_tag_name'] else None

  cards = Card.objects.filter(category__exact=category)
  if style_tag_name:
    cards = cards.filter(style_tag__exact=style_tag_name).order_by("publication_date")
  if time_tag_name:
    cards = cards.filter(time_tag__exact=time_tag_name).order_by("publication_date")
  if function_tag_name:
    cards = cards.filter(function_tag__exact=function_tag_name).order_by("publication_date")
  if region_tag_name:
    cards = cards.filter(region_tag__exact=region_tag_name).order_by("publication_date")

  style_tags_ids = [card.style_tag for card in cards]
  style_tags = StyleTag.objects.filter(pk__in=style_tags_ids).order_by("name")
  function_tags_ids = [card.function_tag for card in cards]
  function_tags = FunctionTag.objects.filter(pk__in=function_tags_ids).order_by("name")
  time_tags_ids = [card.time_tag for card in cards]
  time_tags = TimeTag.objects.filter(pk__in=time_tags_ids).order_by("name")
  region_tags_ids = [card.region_tag for card in cards]
  region_tags = RegionTag.objects.filter(pk__in=region_tags_ids).order_by("name")
  return {"cards" : cards,
          "style_tags" : style_tags,
          "function_tags": function_tags,
          "time_tags": time_tags,
          "region_tags": region_tags,
          "category" : category}