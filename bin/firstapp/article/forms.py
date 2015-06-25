__author__ = 'dmitro'
from django.forms import ModelForm
from article.models import Comments

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
