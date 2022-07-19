import imp
from django.http import QueryDict
from django.shortcuts import render
from articles.models import Article

# Create your views here.
def article_search_view(request):
    print(request.GET)
    query_dict = request.GET
    # query = query_dict.get("query")
    try:
        query = int(query_dict.get("query"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {"object": article_obj}
    return render(request, "articles/search.html", context=context)


def article_create_view(request):
    # print(request.POST)
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title, content)
        article_object = Article.objects.create(title=title, content=content)
        context["object"] = article_object
        context["created"] = True
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)
