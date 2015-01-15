from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from landing import views

urlpatterns = patterns('',
    url(r'^404/$', views.Handle404View.as_view(), name='404'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^$', views.LandingView.as_view(), name='landing'),
)
