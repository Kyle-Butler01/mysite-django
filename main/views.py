from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Products, Card
from .forms import PersonForm, CardBuyForm, RegisterForm
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
    
            

    
