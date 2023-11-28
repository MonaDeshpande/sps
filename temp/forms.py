from django import forms
from django.forms import modelForm
from .models import tempModel

class tempForm(forms.ModelForm):
    class Meta:
        model = tempModel
        fields="__all__"




