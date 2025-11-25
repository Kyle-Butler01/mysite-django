from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Products
from .forms import PersonForm, CardBuyForm
from django.http import HttpResponse


def index (request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


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
        return HttpResponse (request, '<h1>Удаление доступно только при помощи пост запроса<h1>')


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


def buy_method (request):
    if request.method == 'POST':
        form = CardBuyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse(request, '<h1>При добавлении способа оплаты произошла непредвиденная ошибка<h1>')
    else:
        form = CardBuyForm()
        return render(request, 'main/buy_method.html', {'form': form})


# def goods_buy (request, id):
#    num_good = get_object_or_404(Products, id = id)
#     if request.method == 'POST':
#        pass

