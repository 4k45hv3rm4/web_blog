from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Comment
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in (self.fields['username'],self.fileds['password'],self.fields['email']):
            field.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in (self.fields['name'],self.fields['email'],self.fields['body']):
                field.widget.attrs.update({'class':'form-control'})
