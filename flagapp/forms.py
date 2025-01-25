from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'mail', 'contact']

    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Enter your full name', 'class': 'form-control', 'style': 'border-radius: 30px;', 'required': True}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control', 'style': 'border-radius: 30px;', 'required': True}))
    contact = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your contact number', 'class': 'form-control', 'style': 'border-radius: 30px;', 'required': True}))
