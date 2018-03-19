#-*- coding: utf-8 -*-
from django.conf.urls import include, url
import logging, random, hashlib, string
from openpds.connectors.funf import views

urlpatterns = [
    url(r'^set_funf_data$',          views.data),
#    url(r'^set_funf_key$',          views.write_key),
#    url(r'^journal$',               views.journal),
#    url(r'^install_journal$',       views.install_journal),
#    url(r'^config$',                views.config),
#    url(r'^setup$',                 views.setup),
]
