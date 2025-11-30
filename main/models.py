from django.db import models


class Person (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40, unique=False)

    def __str__(self):
        return self.name

class Products (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Card (models.Model):
    id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.card_number
