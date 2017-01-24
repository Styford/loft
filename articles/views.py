# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Article, Comments
from articles.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


# Create your views here.
@csrf_protect
def article(request, article_id=1):
    args = {}
    comment_form = CommentForm
    args["Article"] = Article.objects.get(id=article_id)
    args["Comments"] = Comments.objects.filter(comments_article_id=article_id)
    args["form"] = comment_form
    args["username"] = auth.get_user(request).username
    return render(request, "article.html", args)


def articles(request):
    args = {}
    args["username"] = auth.get_user(request).username
    args["Articles"] = Article.objects.all()
    return render(request,'articles.html', args)


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
    return redirect('/articles/%s/' % article_id)
