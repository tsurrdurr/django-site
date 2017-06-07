from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello World in Django")


def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current time and date: {0}</body></html>".format(now)
    return HttpResponse(html)