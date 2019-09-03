from __future__ import unicode_literals

# from django.conf.urls import url
from django.urls import path

from mezzanine.generic import views


urlpatterns = [
    path("rating/", views.rating, name="rating"),
    path("comment/", views.comment, name="comment"),
]
