from __future__ import unicode_literals

# from django.conf.urls import url
from django.urls import include, re_path, path

from mezzanine.generic import views


urlpatterns = [
    re_path(r"^rating/$", views.rating, name="rating"),
    re_path(r"^comment/$", views.comment, name="comment"),
]
