from django import forms
from .models import administrator_login

class administrator_login_form(forms.ModelForm):
    class Meta:
        model = administrator_login
        fields = ['firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password', 'reenter_password']
        