from django import forms
from .models import Car


class CarFrom(forms.ModelForm):
    class Meta:
        model= Car
        fields = '__all__'

