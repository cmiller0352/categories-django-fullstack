from django.db import models
from django.conf import settings

class Category(models.Model):
  category_name = models.CharField(max_length=100)
  topic = models.CharField(max_length=250)

  def __str__(self):
    return self.category_name

class Post(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  post_name = models.CharField(max_length=100)

  def __str__(self):
    return self.post_name