
from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^1/',views.basic_one),
    url(r'^2/',views.template_two),
    url(r'^3/',views.template_three_simple),
]