import json

from django.views.generic import *
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from django.contrib.auth.forms import PasswordChangeForm

from django.http import HttpResponse, HttpResponseRedirect

from pocket import Pocket

from tellascope.core import forms, models, utils

from tellascope.core.utils import *
from tellascope.config.config import SOCIAL_AUTH_POCKET_CONSUMER_KEY

class JSONResponse(HttpResponse):
    def __init__(self, data, request, *args, **kwargs):
        super(JSONResponse, self).__init__(json.dumps(data), *args, **kwargs)

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class AnonymousRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated(): 
            return HttpResponseRedirect(self.redirect_to)
        return super(AnonymousRequiredMixin, self).dispatch(request, *args, **kwargs)


class LandingView(AnonymousRequiredMixin, TemplateView):
    template_name = 'index.html'
    redirect_to = '/dashboard/'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            user = context['form'].save()
            profile = models.UserProfile.objects.get_or_create(user=user)[0].save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password2'])
            login(request, user)
            return HttpResponseRedirect("/dashboard/")
        else:
            print form.errors
            form = forms.UserCreateForm()
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        form = forms.UserCreateForm(self.request.POST or None)
        context['form'] = form
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    model = models.Article
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        # utils.update_user_pocket(self.request.user)

        context = super(DashboardView, self).get_context_data(**kwargs)
        form = forms.SearchForm(self.request.GET or None)
        context['form'] = form
        context['user'] = self.request.user
        context['uars'] = models.UserArticleRelationship.objects.filter(
                                sharer=self.request.user.profile).order_by("-pocket_date_added")
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        profile = get_object_or_404(models.UserProfile.objects
                .select_related('user__username')
                .filter(user__username=kwargs['username_slug']))
        shares = models.UserArticleRelationship.objects.filter(sharer=profile).annotate(share_count=Count('article__shared_by'))
        context['profile'] = profile
        context['followers'] = profile.get_followers()
        context['following'] = profile.get_following()
        context['shares'] = shares
        return context


class TopicView(LoginRequiredMixin, TemplateView):
    template_name = "topic.html"

    def get_context_data(self, **kwargs):
        print kwargs['topic_slug']
        context = super(TopicView, self).get_context_data(**kwargs)
        topic = get_object_or_404(models.Tag.objects
                .filter(slug=kwargs['topic_slug']))
        context['topic'] = topic
        return context


class SettingsView(FormView):
    template_name = "settings.html"
    form_class = forms.UserProfileSettingsForm

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class LoginView(AnonymousRequiredMixin, TemplateView):
    template_name = 'login.html'
    redirect_to = '/dashboard/'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context['login_form']
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect("/dashboard/")
        else:
            print form.errors
            form = forms.LoginForm()
        return super(LoginView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        login_form = forms.LoginForm(data=self.request.POST or None)
        context['login_form'] = login_form
        return context


class Handle404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super(Handle404View, self).get_context_data(**kwargs)
        return context

