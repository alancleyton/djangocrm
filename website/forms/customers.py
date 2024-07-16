from django import forms
from django.core.exceptions import ValidationError


class CreateForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    phone = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea())

    # def clean(self):
    #     self.add_error(field='first_name', error=ValidationError(message='First name is required', code='is_required'))
    #     return super().clean()
