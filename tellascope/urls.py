from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from core import views

urlpatterns = patterns('',
    url(r'^404/$', views.Handle404View.as_view(), name='404'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
	url(r'^logout/$', views.logout, name='logout'),
)
