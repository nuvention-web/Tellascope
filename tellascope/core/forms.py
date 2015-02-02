from django import forms
from django.utils.translation import ugettext_lazy as _
# from multiselectfield import MultiSelectField

from tellascope.core.models import EMail

class EMailForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(EMailForm, self).__init__(*args, **kwargs)
    #     self.fields['interests'].widget = forms.CheckboxSelectMultiple(choices=self.fields['interests'].choices)

    class Meta:
        model = EMail
        fields = ['email', 'first_name', 'last_name', 'interests']
        labels = {
            'first_name': _('First'),
            'last_name': _('Last'),
            'email': _('Email'),
        }