from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=200, primary_key=True)
  publication_date = models.DateTimeField(auto_now_add=True)


class Text(models.Model):
  text = models.TextField()
  tags = models.ManyToManyField(Tag)
