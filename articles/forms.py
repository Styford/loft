# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Comments, Article

class CommentForm (ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_extraText']

class ArticleForm (ModelForm):
    class Meta:
        model = Article
        fields = ['article_title','article_text']