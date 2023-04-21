from django.shortcuts import render


def home(request):

    return render(request, 'app/pages/home.html')


def login(request):
    return render(request, 'app/pages/login.html')


def create_acount(request):
    return render(request, 'app/pages/create_acount.html')


