#!/usr/bin/python

import sys
import json
import os
from django.core.files.base import ContentFile
from django.utils.timezone import get_current_timezone
from datetime import datetime
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heritage.settings")
django.setup()

from webapp.models import *

SPEC_FILENAME = "spec.json"


def CreateCard(card_json, base_dir):
  tz = get_current_timezone()
  publication_date = tz.localize(
      datetime.strptime(card_json['publication_date'], '%d/%m/%Y'))
  if not Card.objects.filter(title=card_json['title']):
    card = Card(title=card_json['title'],
                subtitle=card_json['subtitle'],
                publication_date=publication_date,
                # cover_image=card_json['cover_image'],
                format=card_json['format'])
    img_path = os.path.join(base_dir, card_json['cover_image'])
    with open(img_path, 'rb') as f:
      card.cover_image.save(card_json['cover_image'], ContentFile(f.read()))
    card.save()
    for a in card_json['authors']:
      if not Author.objects.filter(name=a):
        author = Author(name=a)
        author.save()
        card.authors.add(a)


if __name__ == '__main__':
  assert (len(sys.argv) == 2), '''Path to the test directory should be passed as
   a first argument. It could be a relative or an absolute path. 
   Found argument list: %s''' % str(sys.argv)
  base_dir = sys.argv[1]
  print("Reading the test data from directory: %s...." % base_dir)

  spec_path = os.path.join(base_dir, SPEC_FILENAME)

  with open(spec_path, 'r') as json_data:
    test_data = json.loads(json_data.read())

  for it in test_data["itineraries"]:
    CreateCard(it, base_dir)

  for n in test_data['notes']:
    CreateCard(n, base_dir)
