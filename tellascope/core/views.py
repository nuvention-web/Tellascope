import json

from django.views.generic import TemplateView, RedirectView, FormView, ListView, View
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.forms import PasswordChangeForm

from django.http import HttpResponse, HttpResponseRedirect

from tellascope.core import forms, models

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


class DashboardView(ListView):
    model = models.Article
    template_name = 'dashboard.html'
    object_list = []

    def get_queryset(self):
        form = self.get_context_data()['form']

        if form.is_valid():
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                tag = tag.strip()
            filtered = models.Article.objects.all()
            # if filtered.objects.count() != 0:
            articles = filtered
        else:
            articles = models.Article.objects.all()

        return articles

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        form = forms.SearchForm(self.request.GET or None)
        context['form'] = form
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        profile = get_object_or_404(models.UserProfile.objects
                .select_related('user__username')
                .filter(user__username=kwargs['username_slug']))
        context['profile'] = profile
        return context


class SettingsView(FormView):
    template_name = "settings.html"
    form_class = forms.UserProfileSettingsForm


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class Handle404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super(Handle404View, self).get_context_data(**kwargs)
        return context

