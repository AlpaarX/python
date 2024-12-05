from django import forms
from .models import URL


class ShortenForm(forms.ModelForm):
    class Meta:
        model = URL

        fields = ["url"]
