from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("title", views.title, name="title"),
    path("<str:title>", views.entry, name="entry")
]