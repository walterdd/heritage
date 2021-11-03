#!/usr/bin/python

import sys
import json
import os
from django.core.files.base import ContentFile
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heritage.settings")
django.setup()

from webapp.models import *

SPEC_FILENAME = "spec.json"


def CreateCard(card_json, base_dir):
  img_path = os.path.join(base_dir, card_json['cover_image'])
  with open(img_path, 'rb') as f:
    image = Image()
    image.image.save(card_json['cover_image'], ContentFile(f.read()))
    image.save()
  if not Card.objects.filter(title=card_json['title']):
    card = Card(title=str(card_json['title']),
                subtitle=str(card_json['subtitle']),
                cover_image=image)
    card.save()
    for a in card_json['authors']:
      if not Author.objects.filter(name=a):
        author = Author(name=a)
        author.save()
      card.authors.add(a)
    if card_json['category'] in dict(Article.Category.choices):
      article = Article(text=card_json["text"],
                        category=card_json['category'],
                        card=card)
      article.save()
    else:
      raise NotImplemented("Category is not valid: %s" % card_json["category"])
    card.save()


if __name__ == '__main__':
  assert (len(sys.argv) == 2), '''Path to the test directory should be passed as
   a first argument. It could be a relative or an absolute path. 
   Found argument list: %s''' % str(sys.argv)
  base_dir = sys.argv[1]
  print("Reading the test data from directory: %s...." % base_dir)

  spec_path = os.path.join(base_dir, SPEC_FILENAME)

  with open(spec_path, 'r') as json_data:
    test_data = json.loads(json_data.read())

  for n in test_data['articles']:
    CreateCard(n, base_dir)
