from django import forms
import urllib.request
import json
with urllib.request.urlopen('https://api.exchangerate.host/latest') as url:
    data = json.load(url)

s = data['rates']

currencies_names = s.keys()
currencies_rates = s.values()
convert_list = list(zip(currencies_rates, currencies_names))


def get_key(val):
    for key, value in s.items():
        if val == value:
            return key

    return "key doesn't exist"

class ConverterForm(forms.Form):
    amount = forms.IntegerField()
    current_currency = forms.ChoiceField(choices=convert_list)
    future_currency = forms.ChoiceField(choices=convert_list)
