from dataclasses import field
from django import forms
from .models import ExchangeCrypto

class ExchangeCryptoForm(forms.ModelForm):

    class Meta:
        model = ExchangeCrypto
        fields = ['crypto_value',]