from django.shortcuts import render


def home(request):

    return render(request, 'app/home.html')


def login(request):
    return render(request, 'app/login.html')


def create_acount(request):
    return render(request, 'app/create_acount.html')


