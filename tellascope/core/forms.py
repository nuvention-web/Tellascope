from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from tellascope.core.models import EMail


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
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

class EMailForm(forms.ModelForm):

    class Meta:
        model = EMail
        fields = ['email', 'first_name', 'last_name', 'interests']
        labels = {
            'first_name': _('First'),
            'last_name': _('Last'),
            'email': _('Email'),
        }