from django.conf.urls import url
from siteapp import views

urlpatterns = [
    url(r'^time/$', views.today_is, name='todays_time'),
    url(r'^$', views.index, name='siteapp_index'),
]