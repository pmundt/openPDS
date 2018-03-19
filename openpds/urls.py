from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from openpds.core.tools import v1_api
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from openpds import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='https://github.com/HumanDynamics/openPDS/wiki')),
    url(r'^home/', views.home),
    url(r'^discovery/ping/', views.ping),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/audit', TemplateView.as_view(template_name='audit.html')),
    #(r'^documentation/', include('tastytools.urls'), {'api_name': v1_api.api_name}),
    url(r'^admin/roles', TemplateView.as_view(template_name='roles.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'visualization/', include('openpds.visualization.urls')),
    url(r'^funf_connector/', include('openpds.connectors.funf.urls')),
    #url(r'^funf_connector/', include('openpds.connectors.opensense.urls')),
    url(r'^os_connector/', include('openpds.connectors.opensense.urls')),
    url(r'^survey/', TemplateView.as_view(template_name='survey.html')),
    url(r"meetup/", include("openpds.meetup.urls")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r"accesscontrol/", include("openpds.accesscontrol.urls")),
    url(r'probevisualization/', TemplateView.as_view(template_name='probevisualization.html')),
    url(r'^checkboxes/', TemplateView.as_view(template_name='multiplecheckboxes.html')),
]
