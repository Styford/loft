# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Article, Comments
from articles.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from datetime import datetime
from django.core.paginator import Paginator
import re

# Create your views here.
@csrf_protect
def article(request, article_id=1):
    args = {}
    args["username"] = auth.get_user(request).username
    if args["username"]:
        comment_form = CommentForm
        args["Article"] = Article.objects.get(id=article_id)
        args["Comments"] = Comments.objects.filter(comments_article_id=article_id)
        args["form"] = comment_form
        return render(request, "article.html", args)
    else:
        return redirect("/auth/login/")


def articles(request, page_number=1):
    all_articles = Article.objects.order_by("-article_date")
    current_page = Paginator(all_articles, 5)
    args = {}
    args["username"] = auth.get_user(request).username
    if args["username"]:
        args["Articles"] = current_page.page(page_number)
        return render(request, 'articles.html', args)
    else:
        return redirect("/auth/login/")


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_date = datetime.now()
            comment.comments_author = auth.get_user(request)
            rep_img = re.findall(r'<img[^>]+>', comment.comments_extraText)
            original_img = re.findall(r'<img[^>]+>', comment.comments_extraText)
            i = 0
            for rp in rep_img:
                if re.findall(r'style[^>]+>', rp):
                    rp = rp.replace(re.findall(r'style[^>]+>', rp)[0], "/></div>")
                else:
                    rp = rp.replace(r'/>', "/></div>")
                rep_img[i] = rp.replace('<img',
                                     '<div class="row comment_media"><img class="col-lg-8 col-lg-offset-2 col-md-12 col-sm-12 col-xs-12" ')
                i += 1
            i = 0
            for rp in rep_img:
                comment.comments_extraText = comment.comments_extraText.replace(original_img[i], rep_img[i])
                i += 1
            form.save()
    return redirect('/articles/%s/' % article_id)
