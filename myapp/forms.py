from django import forms
from .models import cmodel

class cform(forms.ModelForm):
    class Meta:
        model = cmodel
        fields = '__all__'
