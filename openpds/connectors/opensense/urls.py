#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from openpds.connectors.opensense import views

urlpatterns = [
    url(r'^upload$',            views.data),
    url(r'^register$',		views.register),
    url(r'^test',		views.test),
    #url(r'^config$',		views.config),
]
