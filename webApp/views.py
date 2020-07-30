from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from webApp.forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from webApp.models import product


def landingpage(request):
    return render(request, 'landing.html')


def register_page(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def products(request):
    images = product.objects.all()
    return render(request, 'product.html', {'pictures': images})


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')
