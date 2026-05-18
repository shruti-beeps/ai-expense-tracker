from django import forms
from .models import Expense
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']