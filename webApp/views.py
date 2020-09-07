from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, forms
from webApp.forms import UserForm, CustomerForm,VehicleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from webApp.models import product,customer
from Automobile_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


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


def service(request):
    return render(request, 'service.html')


def customers_page(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            lname = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            address = request.POST['address']
            mobile_no = request.POST['mobile_no']
            subject = 'Successfully registerd...!'
            message = 'Thanks for connecting with Shree Autombile and car service center.'
            recepient = str(form['email'].value())
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            context = {'sub': subject, 'msg': message, 'res': recepient}
            form.save()
            return render(request, 'thanks.html', context)
    else:
        return render(request, 'customer.html', {'form': CustomerForm})
        

def Vehicle_page(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            type = request.POST['type']
            number = request.POST['number']
            owmer = request.POST['owner']
            form.save()
            return HttpResponse("Thanks for registeration")
    return render(request, 'vehicle.html', {'form': form})
