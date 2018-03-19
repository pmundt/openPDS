from django.conf.urls import include, url
from django.conf import settings
from openpds.accesscontrol.views import storeAccessControl, deleteAccessControl, loadAccessControl, globalAccessControl

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^store/$', storeAccessControl),
    url(r'^load/$', loadAccessControl),
    url(r'^delete/$', deleteAccessControl),
    url(r'^global/$', globalAccessControl),
]
