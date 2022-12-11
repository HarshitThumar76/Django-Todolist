from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Username'
                                   }))

    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control alert-info', 'autocomplete': 'off', 'placeholder': 'Password'
                                   }))


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
