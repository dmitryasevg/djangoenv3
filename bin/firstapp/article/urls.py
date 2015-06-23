
from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^1/',views.basic_one),
    url(r'^2/',views.template_two),
    url(r'^3/',views.template_three_simple),
    url(r'^articles/all/',views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/',views.article),
    url(r'^addlike/(?P<article_id>\d+)',views.addlike),
    url(r'^',views.articles),
]