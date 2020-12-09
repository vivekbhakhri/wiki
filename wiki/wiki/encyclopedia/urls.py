from django.urls import path

from . import views

app_name = 'wiki' #added app name

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry")
]