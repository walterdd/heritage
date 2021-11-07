from .serializers import *
from django.core.paginator import Paginator
from django.http import JsonResponse


def get_paginated_cards_for_category(filter_category, page):
  """Returns JSON with paginated cards filtered by genre and format.

  Args:
    filter_category: card category (Notes or People)
    page: int, page number to fetch

  Returns:
    JSON object with the page of cards and a boolean indicating if there is a
    next page.
  """
  cards = Card.objects.filter(category=filter_category).order_by(
      "publication_date")

  paginator = Paginator(cards, 9, allow_empty_first_page=True)
  cards = paginator.get_page(page)

  return JsonResponse({"cards": CardSerializer(cards, many=True).data,
                       "has_next_page": cards.has_next()})
