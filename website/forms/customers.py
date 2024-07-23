from django import forms
from django.core.exceptions import ValidationError

from website.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'owner', 'company', 'description']