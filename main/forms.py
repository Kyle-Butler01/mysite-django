from django import forms
from .models import Person, Card

class PersonForm (forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'username', 'password']


class CardBuyForm (forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_number', 'CVV']