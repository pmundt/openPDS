from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from openpds.meetup import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^socialHealthRadial', TemplateView.as_view(template_name='visualization/socialHealthRadial.html')),
    url(r'^gfsa', TemplateView.as_view(template_name='visualization/gfsa.html')),
    url(r'^activity', TemplateView.as_view(template_name='visualization/activity.html')),
    url(r'^social', TemplateView.as_view(template_name='visualization/social.html')),
    url(r'^focus', TemplateView.as_view(template_name='visualization/focus.html')),
    url(r'^meetup_home', views.meetup_home),
    url(r'^probe_counts', TemplateView.as_view(template_name='visualization/probeCounts.html')),
    url(r"^places", TemplateView.as_view(template_name='visualization/locationMap.html')),
    url(r'^mitfit/userlocation$', TemplateView.as_view(template_name='visualization/mitfit_user_location.html')),
    url(r'^mitfit/usertime$', TemplateView.as_view(template_name='visualization/mitfit_user_time.html')),
    url(r'^mitfit/recos$', TemplateView.as_view(template_name='visualization/mitfit_recos.html')),
    url(r'^hotspots$', TemplateView.as_view(template_name='visualization/hotspots.html')),
]
