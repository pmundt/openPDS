from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from openpds.meetup.views import update_approval_status, contribute_to_scheduling, create_request, meetup_home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^update_approval_status', update_approval_status),
    url(r'^help_schedule', contribute_to_scheduling),
    url(r'^create_request', create_request),#TemplateView.as_view(template_name="meetup/create_meetup_request.html")),
    url(r'^meetup_home', meetup_home),
]
