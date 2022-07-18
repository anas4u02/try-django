"""
To render HTML pages
"""
import imp
from importlib.resources import path
from random import random
from turtle import title
from unittest.mock import patch
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    print(id)
    random_num = 3
    article_obj = Article.objects.get(id=random_num)

    article_obj.title = "Main Title"
    article_obj.content = "This is the content"

    article_queryset = Article.objects.all()
    # article_obj = Article.objects.create(title="4th", content="Something")

    context = {
        "queryset": article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    HTML_STRING = render_to_string("home-view.html", context=context)

    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)
    # tmpl_string2 = tmpl.render(context=context)

    return HttpResponse(HTML_STRING)
