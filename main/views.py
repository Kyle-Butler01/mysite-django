from itertools import product
from unicodedata import category

from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Products, Card, Seller
from .forms import PersonForm, CardBuyForm, RegisterForm, SellerForm, FormCreateProduct
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')

@login_required()
def show_persons (request):
    persons = Person.objects.all()
    return render(request, 'main/persons.html', {'persons' : persons})


def add_person (request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persons')
        else:
            return HttpResponse ('<h1>Something wrong<h1>')

    else:
        form = PersonForm()
        return render(request,'main/add_person.html', {'form': form})


def delete_person (request, person_id):
    user = get_object_or_404(Person, id = person_id)
    if request.method == 'POST':
        user.delete()
        return redirect('persons')
    else:
        return HttpResponse ('<h1>Удаление доступно только при помощи пост запроса<h1>')


def redact_person (request):
    persons = Person.objects.all()
    return render(request, 'main/redact_person.html', {'persons': persons})


def edit_person (request, id):
    user = get_object_or_404(Person, id = id)
    if request.method == 'POST':
        form = PersonForm (request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('persons')
    else:
        form = PersonForm(instance=user)

    return render(request, 'main/redact_person.html', {'form': form})


def refactor_person (request, id):
    user = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST, instance=user)
    return render(request, 'main/edit_person.html', {'form': form, 'user': user})


def goods (request):
    products = Products.objects.all()
    return render(request, 'main/goods.html', {'products': products})


def add_buy_method (request):
    if request.method == 'POST':
        form = CardBuyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('<h1>При добавлении способа оплаты произошла непредвиденная ошибка<h1>')
    else:
        form = CardBuyForm()
        return render(request, 'main/buy_method.html', {'form': form})

@login_required()
def goods_buy(request, id):
    num_good = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        form = CardBuyForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            cvv = form.cleaned_data['cvv']
            card_exists = Card.objects.filter(
                card_number=card_number,
                cvv=cvv
            ).exists()
            if card_exists:
                return HttpResponse(
                    '<h1>Спасибо за заказ! Ваш заказ в обработке, в течении 15 минут с вами свяжутся. Ожидайте!</h1>')
            else:
                return HttpResponse('<h1>При обработке заказа произошла ошибка!</h1>')
        else:
            return HttpResponse('<h1>При заполнении формы произошла ошибка, попробуйте заново<h1>')

    else:
        form = CardBuyForm()
        return render(request, 'main/buy.html', {'form': form, 'product': num_good})


def register (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('index')
        else:
            return HttpResponse ('<h1>Что-то не так заполните форму еще раз и повторите попытку</h1>')
    else:
        form = RegisterForm()

        return render (request, 'main/register.html', {'form': form})


def seller_log (request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            unique_pass = form.cleaned_data['unique_pass']
            login_name = form.cleaned_data['login_name']

            seller_exist = Seller.objects.filter(
                name=name,
                unique_pass = unique_pass,
                login_name=login_name,
            ).exists()

            if seller_exist:
                products = Products.objects.all()
                return redirect('seller_page')
            else:
                return HttpResponse ('<h2>Кажется такого пользователя не существует, повторите попытку позже</h2>')

        else:
            return HttpResponse ('<h2><При заполнении формы произошла ошибка, пожалуйста заполните форму правильно и повторите попытку/h2>')

    else:
        form = SellerForm()
        return render(request, 'main/seller_log.html', {'form': form})


def create_goods (request):
    if request.method == 'POST':
        form = FormCreateProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            product_exist = Products.objects.filter(
                name=name,
                category=category
            ).exists()

            if product_exist:
                return HttpResponse ('<h2>Добавляемый вами продукт уже находится в магазине, пожалуйста, попробуйте что-то другое</h2>')
            else:
                form.save()
                return redirect('seller_page')
        else:
            return HttpResponse ('<h2>При заполнении формы произошла ошибка, проверьте правильность данных и попробуйте еще раз</h2>')
    else:
        form = FormCreateProduct()
        return render(request, 'main/create_good.html', {'form':form})


def seller_page (request):
    products = Products.objects.all()
    return render(request, 'main/goods_seller.html', {'products': products})

    
