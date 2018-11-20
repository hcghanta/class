from django import forms
from .models import Currency



class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['symbol','value_convert']


