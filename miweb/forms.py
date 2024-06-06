from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Email',
            'message': 'Mensaje',
        }
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'form-control'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tu mensaje', 'rows': 3, 'class': 'form-control'}),
        }