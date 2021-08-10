import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from products.forms import ProductForm
from products.models import Product, ConfirmCode


# Create your views here.


def hello_world_view(request):
    return HttpResponse('<h1>Hello World!!!</h1>')


PAGE_SIZE = 2


def main_page_view(request):
    page = int(request.GET.get('page', '1'))  # 1, 2
    print('Страница:', page)
    print(f'Объекты: [{(page - 1) * PAGE_SIZE}:{page * PAGE_SIZE}]')
    products = Product.objects.all()
    total = products.count()
    page_count = total // PAGE_SIZE  # 6 // 3 == 1
    if total % PAGE_SIZE > 0:  # 6 % 3 = 1 > 0
        page_count += 1
    next_page = page + 1
    prev_page = page - 1
    data = {
        'title': 'Главная страница',
        'page': page,
        'next_page': next_page,
        'prev_page': prev_page,
        'last_page': page_count,
        'page_count': range(1, page_count + 1),
        'product_list': products[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]  # 2 --> [2:4]  3 --> [4:6]
    }
    return render(request, 'index.html', context=data)


def product_item_view(request, product_id):
    product = Product.objects.get(id=product_id)
    data = {
        'product': product, 'title': product.title
    }
    return render(request, 'item.html', context=data)


@login_required(login_url='/login/')
def add_product(request):
    if request.method == 'GET':
        data = {
            'form': ProductForm()
        }
        return render(request, 'add.html', context=data)
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/login/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    data = {
        'form': LoginForm()
    }
    return render(request, 'login.html', context=data)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            data = {
                'form': form,
            }
            return render(request, 'register.html', context=data)
    data = {
        'form': RegisterForm()
    }
    return render(request, 'register.html', context=data)


def search(request):
    query = request.GET.get('query', '')
    print(query)
    products = Product.objects.filter(title__contains=query)
    print(products.values())
    return JsonResponse(data={'list': list(products.values())}, safe=False)


def javascript(request):
    return render(request, 'javascript.html')


def activate(request, code):
    print(code)
    try:
        user = ConfirmCode.objects.get(code=code, valid_until__dte=datetime.datetime.now()).user
        user.is_active = True
        user.save()
    except:
        pass
    return redirect('/login/')
