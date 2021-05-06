from django.shortcuts import render
from django.http import HttpResponse
from .models import Text
import numpy as np


def landing_page(request):
  texts = Text.objects.all()
  context = {'texts': texts}
  return render(request, 'landing_page.html', context)