"""
URL configuration for shortly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.shorten, name='shorten')
Class-based views
    1. Add an import:  from other_app.views import shorten
    2. Add a URL to urlpatterns:  path('', shorten.as_view(), name='shorten')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("devshortly.urls")),
    path("<slug:slug>", include("devshortly.urls")),
]
