from django.urls import path
from . import views

urlpatterns = [
    path("", views.shorten, name="shorten"),
    path("i/<slug:slug>", views.slug_redirect, name="slug_redirect"),
]
