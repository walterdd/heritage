from django.shortcuts import render
from .models import *
from .utils import get_cards_and_tags_for_format, get_cards_and_tags_for_format
from django.views import View
from django.http import JsonResponse
from .serializers import *
from django.core.paginator import Paginator


class LandingPage(View):
  """Serializes data to JSON for the landing page.
  """
  def get(self, request, it_page=1, text_page=1):
    categories = Category.objects.all().order_by("title")
    publications = Publication.objects.all().order_by("publication_date")
    itineraries = Card.objects.filter(format='ITINERARIES').order_by("publication_date")
    cards = Card.objects.all().order_by("publication_date")

    it_paginator = Paginator(itineraries, 4, allow_empty_first_page=True)
    text_paginator = Paginator(cards, 3, allow_empty_first_page=True)
    itineraries = it_paginator.get_page(it_page)
    cards = text_paginator.get_page(text_page)

    data = {"categories" : CategorySerializer(categories, many=True).data,
     "publications": PublicationSerializer(publications, many=True).data,
     "itineraries" : CardSerializer(itineraries, many=True).data,
     "cards" : CardSerializer(cards, many=True).data,
     "has_more_cards" : cards.has_next(),
     "has_more_itineraries" : itineraries.has_next()}
    return JsonResponse(data)


class NotesList(View):
  """Serializes data to JSON with the cards for Notes format.

  Args:
    request: HttpRequest, if request GET attribute contains 'tag_name', the
     results will be filtered by the tag.
  """
  def get(self, request, *args, **kwargs):
    format = Card.Format.NOTES
    data = get_texts_and_tags_for_format(format, request)
    return JsonResponse(data)


class PeopleList(View):
  """Serializes data to JSON with the cards for People format.
  """
  def get(self, request, *args, **kwargs):
    format = Card.Format.PEOPLE
    data = get_texts_and_tags_for_format(format, request)
    return JsonResponse(data)


class MonumentsList(View):
  """Serializes data to JSON with the cards for Monument format.
  """
  def get(self, request, *args, **kwargs):
    format = Card.Format.CARDS
    data = get_cards_and_tags_for_format(format, request)
    return JsonResponse(data)


class CardView(View):
  """Renders a template for the page with a text given text primary key.
  """
  def get(self, request):
    """
    :param request: HttpRequest, must contain 'text_id' in GET attributes.
    :return: HttpResponse with a rendered template.
    """
    card_pk = request.GET['card_id']
    card = Card.objects.get(id=card_pk)
    data = {"card": CardSerializer(card).data}
    return JsonResponse(data)
