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


def CreateImage(file_name, dir_path):
  img_path = os.path.join(dir_path, file_name)
  with open(img_path, 'rb') as f:
    image = Image()
    image.image.save(file_name, ContentFile(f.read()))
    image.save()
  return image


def CreateCard(card_json, dir_path):
  image = CreateImage(card_json['cover_image'], dir_path)
  assert card_json['category'] in dict(Card.Category.choices), "Given unknown " \
                                                               "category: %s"\
                                                               % card_json[
                                                                 'category']
  if not Card.objects.filter(title=card_json['title']):
    card = Card(id=str(card_json['id']),
                title=str(card_json['title']),
                subtitle=str(card_json['subtitle']),
                category=card_json['category'],
                cover_image=image)
    card.save()
    for a in card_json['authors']:
      if not Author.objects.filter(name=a):
        author = Author(name=a)
        author.save()
      card.authors.add(a)
    article = Article(text=card_json["text"],
                      card=card)
    article.save()
    card.save()


def CreatePublication(pub_json, dir_path):
  image = CreateImage(pub_json['cover_image'], dir_path)
  pub = Publication(title=pub_json['title'], subtitle=pub_json['subtitle'],
                    cover_image=image)
  pub.save()
  for card in pub_json["cards"]:
    pub.cards.add(Card.objects.get(pk=card['id']))


if __name__ == '__main__':
  assert (len(sys.argv) == 2), '''Path to the test directory should be passed as
   a first argument. It could be a relative or an absolute path. 
   Found argument list: %s''' % str(sys.argv)
  dir_path = sys.argv[1]
  print("Reading the test data from directory: %s...." % dir_path)

  spec_path = os.path.join(dir_path, SPEC_FILENAME)

  with open(spec_path, 'r') as json_data:
    test_data = json.loads(json_data.read())

  for n in test_data['articles']:
    CreateCard(n, dir_path)

  for pub in test_data['publications']:
    CreatePublication(pub, dir_path)
