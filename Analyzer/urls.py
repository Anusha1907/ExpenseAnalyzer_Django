from django.conf.urls import url
from Analyzer import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]
