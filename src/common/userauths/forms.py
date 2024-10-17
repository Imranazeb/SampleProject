from typing import Any
from common.userauths.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_bootstrap5.bootstrap5 import FloatingField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'username',  'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].label = 'Username (lower case only and no spaces)'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Re-enter Password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


            
        

    # This is an interal Django function and we are overwriting it (esplanation: https://github.com/pennersr/django-allauth/blob/4bb9e0170f37d8196bd0c4a78e83adb7b779c113/allauth/account/adapter.py#L175)
    def clean_email(self): 
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already taken")

        if len(email) > 255 or len(email) < 5:
            raise forms.ValidationError("Email is invalid")
        
        return email