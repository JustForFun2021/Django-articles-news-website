from django import forms
from .models import Contact

class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        #What we want to display in our form
        fields = ('name','email','message')
    