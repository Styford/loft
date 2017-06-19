# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.



class Article(models.Model):
    class Meta:
        db_table = "article"  # Название таблицы в БД
        verbose_name = "Статья"  # Название модели в админке в единственном числе
        verbose_name_plural = "Статьи"  # Название модели в админке во множественном числе

    article_title = models.CharField(max_length=200, verbose_name="Заголовок статьи")
    article_text = RichTextUploadingField(verbose_name="Текст статьи", blank=True, default='')
    article_date = models.DateTimeField(verbose_name="Дата публикации")
    # article_likes = models.IntegerField(default=0)
    article_author = models.ForeignKey(User)

    def __unicode__(self):  # Название объекта в админке
        return self.article_title


class Comments(models.Model):
    class Meta:
        db_table = "comments"  # Название таблицы в БД
        verbose_name = "Комментарий"  # Название модели в админке в единственном числе
        verbose_name_plural = "Комментарии"  # Название модели в админке во множественном числе


    comments_article = models.ForeignKey(Article, verbose_name="Статья")
    comments_author = models.ForeignKey(User, verbose_name="Автор комментария", blank=True)
    comments_date = models.DateTimeField(blank=True)
    comments_extraText = RichTextUploadingField(verbose_name="Ваш комментарий", blank=True, default='')

