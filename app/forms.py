from django.forms import ModelForm, Textarea, TextInput
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput(attrs={'class': 'form-control','placeholder':'Name '}),
            'subject' : TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'form-control','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'form-control w-100','placeholder':'Your Message','rows':'5'}),
        }