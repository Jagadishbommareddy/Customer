from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from Tagent.views import *
router = routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)
router.register(r'address',AddressViewSet)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('Tagent.urls')),
url(r'^', include(router.urls)),
]

