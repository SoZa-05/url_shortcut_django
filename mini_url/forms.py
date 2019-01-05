from django.forms import ModelForm

from .models import MiniUrl


class UrlForm(ModelForm):
    class Meta:
        model = MiniUrl
        fields = ['url_long', 'pseudo']
