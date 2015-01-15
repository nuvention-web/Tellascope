import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView, View
import requests

from tellascope.landing.models import EMail


class JSONResponse(HttpResponse):
    def __init__(self, data, request, *args, **kwargs):
        super(JSONResponse, self).__init__(json.dumps(data), *args, **kwargs)

class LandingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        # posts = (Post.objects.all()
        #         .filter(status='p')
        #         .select_related('author')
        #         .order_by('-posted_datetime'))
        # context['posts'] = posts
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        # posts = (Post.objects.all()
        #         .filter(status='p')
        #         .select_related('author')
        #         .order_by('-posted_datetime'))
        # context['posts'] = posts
        return context


class Handle404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super(Handle404View, self).get_context_data(**kwargs)
        return context

