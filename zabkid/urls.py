"""zabkid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework.views import APIView

from django.conf import settings
from django.conf.urls.static import static
from django_filters.views import FilterView

from django.conf.urls import url
from django.urls import re_path
from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from . import views
from .views import Online_RideViewSet

router = routers.DefaultRouter()

router.register('driver', views.DriverAPI)
router.register('childrens', views.ChildrensAPI)
router.register('ride_history', views.RideHistoryAPI)
router.register('parent', views.ParentAPI)
router.register('shifts', views.ShiftsAPI)
router.register('online_ride', Online_RideViewSet)
router.register('add_assign_driver', views.AddAssignDriverAPI)
router.register('assign_driver', views.AssignDriverAPI)
router.register('add_ride_history', views.ADDRideHistoryAPI)


urlpatterns = [
    # path('', views.index, name='index'),
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/driver/<int:id>', views.getDriver.as_view()),
    url('^api/driver1(?P<contact_number>.+)/$', views.getDriver1.as_view())
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)