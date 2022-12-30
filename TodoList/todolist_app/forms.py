from django import forms
from django.contrib.auth.models import User
from .models import TodoItem
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Username', 'help_text': 'Enter Valid username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'name@example.com'}),
        }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control alert-info', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                   'class': 'form-control alert-info',  'placeholder': 'Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_list = list(
            map(lambda lm: lm[0], User.objects.values_list('username').distinct()))
        if username in username_list:
            raise forms.ValidationError('Please enter a uniqe username')
        return username


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Username'
                                   }))

    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'type': 'password', 'autocomplete': 'off', 'placeholder': 'Password'
                                   }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_list = list(
            map(lambda lm: lm[0], User.objects.values_list('username').distinct()))
        if not username in username_list:
            raise forms.ValidationError('User is not Found!! Please Signup')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Incorrect Password')
        return password


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'titlehelp', 'placeholder': 'Enter Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Description'}),
        }


class TodoListSearchForm(forms.Form):
    search_string = forms.CharField(label='', max_length=50,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control mr-sm-2', 'type': 'search', 'placeholder': 'Search...', 'aria-label': 'Search'
                                        }))
