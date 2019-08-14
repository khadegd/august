from __future__ import unicode_literals

from django.urls import include, path, re_path
# from django.conf.urls import url
from django.contrib.auth import views as auth_views

from mezzanine.conf import settings
from mezzanine.core import views as core_views


urlpatterns = []

if "django.contrib.admin" in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r"^password_reset/$",
            auth_views.PasswordResetView.as_view(),
            name="password_reset"),
        re_path(r"^password_reset/done/$",
            auth_views.PasswordResetDoneView.as_view(),
            name="password_reset_done"),
        re_path(r"^reset/done/$",
            auth_views.PasswordResetCompleteView.as_view(),
            name="password_reset_complete"),
        re_path(r"^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$",
            auth_views.PasswordResetConfirmView.as_view(),
            name="password_reset_confirm"),
    ]

urlpatterns += [
    re_path(r"^edit/$", core_views.edit, name="edit"),
    re_path(r"^search/$", core_views.search, name="search"),
    re_path(r"^set_site/$", core_views.set_site, name="set_site"),
]
