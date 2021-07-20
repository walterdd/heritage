from .serializers import *
from django.core.paginator import Paginator
from django.http import JsonResponse

def get_paginated_cards_for_genre_and_format(format, genre, page):
  """Returns JSON with paginated cards filtered by genre and format.

  Args:
    format: card format (Notes or People)
    genre: card genre (such as story, interview, guidebook etc.)
    page: int, page number to fetch

  Returns:
    JSON object with the page of cards and a boolean indicating if there is a
    next page.
  """
  cards = Card.objects.filter(format__exact=format).order_by("publication_date")
  if genre:
    if format == Card.Format.NOTES:
      cards = cards.filter(note__genre__name=genre).order_by("publication_date")
    elif format == Card.Format.PEOPLE:
      cards = cards.filter(person__genre__name=genre).order_by("publication_date")

  paginator = Paginator(cards, 9, allow_empty_first_page=True)
  cards = paginator.get_page(page)

  return JsonResponse({"cards" : CardSerializer(cards, many=True).data,
                       "has_next_page" : cards.has_next()})
