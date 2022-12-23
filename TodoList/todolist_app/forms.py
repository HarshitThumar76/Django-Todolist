from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Username', 'help_text': 'Enter Valid username'
                                   }))

    firstname = forms.CharField(label='First Name', max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'First Name'
                                    }))

    lastname = forms.CharField(label='Last Name', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Last Name'
                                   }))

    email = forms.EmailField(label='Email address', max_length=50,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control alert-info', 'type': 'email', 'autocomplete': 'off', 'placeholder': 'name@example.com'
                                 }))

    password = forms.CharField(label='Choose Password', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'type': 'password', 'autocomplete': 'off', 'placeholder': 'Password'
                                   }))

    password_confirm = forms.CharField(label='Confirm Password', max_length=50,
                                       widget=forms.TextInput(
                                           attrs={
                                               'class': 'form-control alert-info', 'type': 'password', 'autocomplete': 'off', 'placeholder': 'Password'
                                           }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_list = list(
            map(lambda lm: lm[0], User.objects.values_list('username').distinct()))
        if username in username_list:
            raise forms.ValidationError('Please enter a uniqe username')
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(
                'Your password and confirmation password do not match.')
        return password_confirm


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


class TodoListForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control', 'aria-describedby': 'titlehelp', 'placeholder': 'Enter Title'
                                }))

    description = forms.CharField(label='Description', max_length=1000,
                                  widget=forms.Textarea(
                                      attrs={
                                        'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Description'
                                      }))


class TodoListSearchForm(forms.Form):
    search_string = forms.CharField(label='', max_length=50,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control mr-sm-2', 'type': 'search', 'placeholder': 'Search...', 'aria-label': 'Search'
                                        }))
