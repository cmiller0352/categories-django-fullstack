from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ('category_name', 'topic') # not sure about this

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('post_name', 'category')
