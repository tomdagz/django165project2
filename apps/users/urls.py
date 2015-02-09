from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^login/$', 'apps.users.views.userloguin', name="login"),
    url(r'^salir/$', 'apps.users.views.LogOut', name="logout"),

)
