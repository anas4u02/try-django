"""
To render HTML pages
"""
import imp
from random import random
from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    random_num = 3
    article_obj = Article.objects.get(id=random_num)

    article_obj.title = "Main Title"
    article_obj.content = "This is the content"

    article_title = article_obj.title
    article_content = article_obj.content

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    HTML_STRING = """
    """.format(
        **context
    )

    return HttpResponse(HTML_STRING)
