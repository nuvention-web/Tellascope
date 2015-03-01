from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm, AuthenticationForm
from django.core.exceptions import ValidationError

from tellascope.core import models
from taggit.forms import *

from tellascope.config.config import *

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class UserCreateForm(UserCreationForm):
    def validate_unique_email(email):
        if email and User.objects.filter(email=email).count() > 0:
            raise ValidationError(u'This email address is already registered.')

    email = forms.EmailField(required=True, validators=[validate_unique_email])

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Pick a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['password1'].help_text = "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
        self.fields['password2'].help_text = "Enter the same password as above, for verification."

class UserProfileSettingsForm(forms.ModelForm):
    
    class Meta:
        model = models.UserProfile
        exclude = ['twitter_username', 'twitter_description', 'twitter_profile_picture']


class SearchForm(forms.Form):
    tags = forms.CharField(max_length=250, required=True)




