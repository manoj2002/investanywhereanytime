from django import forms
from django.contrib.auth.forms import UserCreationForm
class TickerForm(forms.Form):
    ticker= forms.CharField(label="Ticker" ,max_length=5)
