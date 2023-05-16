
from .models import Contact
from django import forms


class FormContact(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['name','email','subject','message']