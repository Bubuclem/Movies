from django.forms import ModelForm, EmailInput, PasswordInput, TextInput
from django.contrib.auth.models import User

ATTRS_CLASS = 'w-full px-4 py-3 rounded-md dark:border-coolGray-700 dark:bg-coolGray-900 dark:text-coolGray-100'

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
        'email' : EmailInput(attrs={'class':ATTRS_CLASS}),
        'password' : PasswordInput(attrs={'class':ATTRS_CLASS}),
        }

class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RegistreAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        widgets = {
        'username' : TextInput(attrs={'class':ATTRS_CLASS}),
        'first_name' : TextInput(attrs={'class':ATTRS_CLASS}),
        'last_name' : TextInput(attrs={'class':ATTRS_CLASS}),
        'email' : EmailInput(attrs={'class':ATTRS_CLASS}),
        'password' : PasswordInput(attrs={'class':ATTRS_CLASS}),
        }