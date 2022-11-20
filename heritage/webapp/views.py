from .utils import get_paginated_cards_for_category
from django.views import View
from django.http import JsonResponse
from .serializers import *
from django.core.paginator import Paginator


class LandingPage(View):
  """Serializes data to JSON for the landing page.
  """
  def get(self, request, it_page=1, text_page=1):
    publications = Publication.objects.all().order_by("publication_date")
    itineraries = Card.objects.filter(
        category=Card.Category.ITINERARY).order_by(
        "publication_date")
    cards = Card.objects.all().order_by("publication_date")

    it_paginator = Paginator(itineraries, 4, allow_empty_first_page=True)
    text_paginator = Paginator(cards, 9, allow_empty_first_page=True)
    itineraries = it_paginator.get_page(it_page)
    cards = text_paginator.get_page(text_page)

    data = {"publications": PublicationSerializer(publications, many=True).data,
     "itineraries" : CardSerializer(itineraries, many=True).data,
     "cards" : CardSerializer(cards, many=True).data,
     "has_more_cards" : cards.has_next(),
     "has_more_itineraries" : itineraries.has_next()}
    return JsonResponse(data)


class NotesList(View):
  """Serializes data to JSON with the cards for Notes category.
  """
  def get(self, request, genre=None, page=1):
    filter_category = Card.Category.NOTE
    return get_paginated_cards_for_category(filter_category, page)


class PeopleList(View):
  """Serializes data to JSON with the cards for People category.
  """
  def get(self, request, genre=None, page=1):
    filter_category = Card.Category.PEOPLE
    return get_paginated_cards_for_category(filter_category, page)


class MonumentList(View):
  """Serializes data to JSON with the cards for Monument category.
  """
  def get(self, request, genre=None, page=1):
    filter_category = Card.Category.MONUMENT
    return get_paginated_cards_for_category(filter_category, page)


class ArticleView(View):
  """Renders a template for the page with an article given the primary key.
  """
  def get(self, request, article_id):
    """
    :param request: HttpRequest, must contain 'text_id' in GET attributes.
    :return: HttpResponse with a rendered template.
    """
    article = Article.objects.get(id=article_id)
    data = {"article": ArticleSerializer(article).data}
    return JsonResponse(data)
