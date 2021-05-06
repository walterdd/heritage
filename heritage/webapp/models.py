from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=200, primary_key=True)

class Image(models.Model):
  image = models.ImageField()

class Text(models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField()
  author = models.CharField(max_length=30)
  tags = models.ManyToManyField(Tag)
  images = models.ManyToManyField(Image)
  publication_date = models.DateTimeField(auto_now_add=True)
  category = models.TextChoices("category", "МАРШРУТЫ ЗАМЕТКИ ЛЮДИ КАРТОТЕКА")

