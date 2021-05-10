from django.shortcuts import render
from django.http import HttpResponse
from .models import Text
from rest_framework import generics
from .serializers import TextSerializer


def landing_page(request):
  texts = Text.objects.all()
  context = {'texts': texts}
  return render(request, 'landing_page.html', context)


class TextList(generics.ListCreateAPIView):
  queryset = Text.objects.all()
  serializer_class = TextSerializer