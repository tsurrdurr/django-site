from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime

def index(request):
    return HttpResponse("Hello World in Django")

def blog(request):
    x = TemplateResponse(request, 'post.html', {})
    x.render()
    return HttpResponse(x)


def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current time and date: {0}</body></html>".format(now)
    return HttpResponse(html)