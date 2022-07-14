"""
To render HTML pages
"""
from django.http import HttpResponse


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Anas"
    print(100 * 200)
    HTML_STRING = f"""
    <h1>Hello {name}</h1>
    """

    return HttpResponse(HTML_STRING)
