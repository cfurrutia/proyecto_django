from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Email',
            'message': 'Mensaje',
        }
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'id': 'form4Example1', 
                'class': 'form-control', 
                'data-mdb-input-init': True,
                'placeholder': ' '
            }),
            'customer_email': forms.EmailInput(attrs={
                'id': 'form4Example2', 
                'class': 'form-control', 
                'data-mdb-input-init': True,
                'placeholder': ' '
            }),
            'message': forms.Textarea(attrs={
                'id': 'form4Example3', 
                'class': 'form-control', 
                'data-mdb-input-init': True, 
                'rows': 4,
                'placeholder': ' '
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ContactFormForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] += ' form-outline mb-4'
