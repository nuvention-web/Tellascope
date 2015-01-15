from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from tellascope.landing.models import EMail

class EMailForm(ModelForm):
    class Meta:
        model = EMail
        fields = ['email', 'first_name', 'last_name']
        labels = {
            'first_name': _('First'),
            'last_name': _('Last'),
            'email': _('Email'),
        }