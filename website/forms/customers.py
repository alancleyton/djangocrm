from django import forms
from django.core.exceptions import ValidationError

CHOICES = [('Option 1', 'Option 1'),('Option 2', 'Option 2')]

class CreateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('all_users')
        self.companies = kwargs.pop('all_companies')
        super(CreateForm, self).__init__(*args, **kwargs)
        
        users_choices = tuple([(user['id'], user['username']) for user in self.users])
        companies_choices = tuple([(company['id'], company['name']) for company in self.companies])
        
        self.fields['owner'] = forms.ChoiceField(choices=users_choices)
        self.fields['company'] = forms.ChoiceField(choices=companies_choices)

    first_name = forms.CharField(widget=forms.TextInput(), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(), max_length=50)
    phone = forms.CharField(widget=forms.TextInput(), max_length=30)
    description = forms.CharField(widget=forms.Textarea())
