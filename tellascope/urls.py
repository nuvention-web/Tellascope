from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from core import views

urlpatterns = patterns('',
    url(r'^404/$', views.Handle404View.as_view(), name='404'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^u/(?P<username_slug>[-\w]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^topic/(?P<topic_slug>[-\w]+)/$', views.TopicView.as_view(), name='topic'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^dashboard/private/$', views.PrivateDashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/public/$', views.PublicDashboardView.as_view(), name='dashboard'),

    # APIs
    url(r'^api/uar/post/makepublic/$', views.MakeUARPublicView.as_view(), name='makepublic'),
    url(r'^api/user/post/refreshpocket/$', views.UpdateUserPocket.as_view(), name='updatepocket')
)

