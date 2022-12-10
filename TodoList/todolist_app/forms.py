from django import forms


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
