from django import forms
from .models import QuoteRequest, NewsletterSubscription

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'service', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Your Name',
                'style': 'height: 55px;',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Your Email',
                'style': 'height: 55px;',
                'required': 'required'
            }),
            'service': forms.Select(attrs={
                'class': 'form-select border-0',
                'style': 'height: 55px;',
                'required': 'required'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Your Phone',
                'style': 'height: 55px;',
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Special Note',
                'rows': 4,
                'required': 'required'
            }),
        }

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-transparent w-100 py-3 ps-4 pe-5',
                'placeholder': 'Your Email',
                'required': 'required'
            }),
        }
