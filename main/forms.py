from django import forms
from .models import Person, Card
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonForm (forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'username', 'password']


class CardBuyForm (forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_number', 'cvv']



class RegisterForm (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']