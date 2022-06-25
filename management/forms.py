from django.forms import ModelForm, EmailInput, PasswordInput, TextInput, Textarea
from django.contrib.auth.models import User

from management.models import Review

INPUT_CLASS = 'focus:ring-purple-500 focus:border-purple-500 flex-grow block w-full min-w-0 rounded-md sm:text-sm border-gray-300'
TEXTAREA_CLASS = 'shadow-sm focus:ring-purple-500 focus:border-purple-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md'

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': EmailInput(attrs={'class': INPUT_CLASS}),
            'password': PasswordInput(attrs={'class': INPUT_CLASS}),
        }

class AccountForm(ModelForm):
    ''' Account form
    '''
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
        'username' : TextInput(attrs={'class':INPUT_CLASS}),
        'email' : EmailInput(attrs={'class':INPUT_CLASS}),
        'first_name' : TextInput(attrs={'class':INPUT_CLASS}),
        'last_name' : TextInput(attrs={'class':INPUT_CLASS}),
        }

class RegistreAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels = {
        'content': 'Commentaire'
        }
        widgets = {
        'content': Textarea(attrs={'class':TEXTAREA_CLASS})
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
        'username': 'Pseudo',
        'first_name': 'Prénom',
        'last_name': 'Nom',
        'email': 'Email'
        }
        widgets = {
        'username': TextInput(attrs={'class':INPUT_CLASS}),
        'first_name': TextInput(attrs={'class':INPUT_CLASS}),
        'last_name': TextInput(attrs={'class':INPUT_CLASS}),
        'email': EmailInput(attrs={'class':INPUT_CLASS}),
        }