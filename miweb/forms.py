from django import forms
from .models import ContactForm
        
class ContactFormForm(forms.Form):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}))
    customer_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Tu correo electrónico'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu mensaje'}))


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']