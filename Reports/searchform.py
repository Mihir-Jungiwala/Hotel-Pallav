# forms.py
from django import forms

class GeneralSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
