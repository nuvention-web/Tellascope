from django.forms import ModelForm

from tellascope.landing.models import EMail

class EMailForm(ModelForm):
    class Meta:
        model = EMail,
        fields = ['email', 'first_name', 'last_name']