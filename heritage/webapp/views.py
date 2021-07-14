from django.shortcuts import render
from .models import *
from .utils import get_texts_and_tags_for_category, get_cards_and_tags_for_category
from django.views import View
from django.http import JsonResponse
from .serializers import *


class LandingPage(View):
  """Renders a template for the landing page.

  Returns:
    HttpResponse object with a rendered template.
    Template takes two args:
      publications: QuerySet of all publications ordered by the publication date.
      collections: QuerySet of all collections ordered by the publication date.
  """
  def get(self, request, *args, **kwargs):
    collections = Collection.objects.all().order_by("publication_date")
    publications = Publication.objects.all().order_by("publication_date")
    data = {"collections" : CollectionSerializer(collections, many=True).data,
     "publications": PublicationSerializer(publications, many=True).data}
    return JsonResponse(data)
#     return render(request, template_name="landing_page.html", context=data)


class NotesList(View):
  """Renders a template for the page with texts from the Notes category.

  Args:
    request: HttpRequest, if request GET attribute contains 'tag_name', the results
      will be filtered by the tag.
  Returns:
    HttpResponse object with a rendered template.
    Template takes two args:
      texts: QuerySet of all texts from the Notes category ordered by the
       publication date.
      tags: QuerySet of tags attributed to the selected texts in alphabetical
       order.
  """
  def get(self, request, *args, **kwargs):
    category = Text.Category.NOTES
    data = get_texts_and_tags_for_category(category, request)
    return render(request, template_name="texts.html", context=data)


class PeopleList(View):
  """Renders a template for the page with texts from the People category.

  Args:
    request: HttpRequest, if request GET attribute contains 'tag_name', the results
      will be filtered by the tag.
  Returns:
    HttpResponse object with a rendered template.
    Template takes two args:
      texts: QuerySet of all texts from the People category ordered by the
       publication date.
      tags: QuerySet of tags attributed to the selected texts in alphabetical
       order.
  """
  def get(self, request, *args, **kwargs):
    category = Text.Category.PEOPLE
    data = get_texts_and_tags_for_category(category, request)
    return render(request, template_name="texts.html", context=data)


class CardsList(View):
  """Renders a template for the page with texts from the People category.

  Returns:
    HttpResponse object with a rendered template.
    Template takes two args:
      texts: QuerySet of all texts from the People category ordered by the
       publication date.
      tags: QuerySet of tags attributed to the selected texts in alphabetical
       order.
  """
  def get(self, request, *args, **kwargs):
    category = Text.Category.CARDS
    data = get_cards_and_tags_for_category(category, request)
    return render(request, template_name="cards.html", context=data)


class Text(View):
  """Renders a template for the page with a text given text primary key.
  """
  def get(self, request):
    """
    :param request: HttpRequest, must contain 'text_id' in GET attributes.
    :return: HttpResponse with a rendered template.
    """
    text_pk = request.GET['text_id']
    text = Text.objects.get(id=text_pk)
    data = {"text": text}
    return render(request, template_name="text.html", context=data)
