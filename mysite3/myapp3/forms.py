from django import forms


class FiboForm(forms.Form):
    num = forms.CharField(label='num')
