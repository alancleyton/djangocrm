from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from website.models import Customer, Company


CHOICES = [('Option 1', 'Option 1'),('Option 2', 'Option 2')]

class CreateForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(), max_length=50)
    phone = forms.CharField(widget=forms.TextInput(), max_length=30)
    description = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users')
        self.companies = kwargs.pop('companies')
        super(CreateForm, self).__init__(*args, **kwargs)
        
        users_choices = tuple([(user['id'], user['username']) for user in self.users])
        companies_choices = tuple([(company['id'], company['name']) for company in self.companies])
        
        self.fields['owner'] = forms.ChoiceField(choices=users_choices)
        self.fields['company'] = forms.ChoiceField(choices=companies_choices)

    def save(self):
        data = self.cleaned_data
        data['company'] = Company.objects.get(pk=data['company'])
        data['owner'] = User.objects.get(pk=data['owner'])
        customer = Customer(**data)
        customer.save()
