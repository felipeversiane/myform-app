from django.shortcuts import render


def home(request):

    return render(request, 'app/pages/home.html')


def login(request):
    return render(request, 'app/pages/login.html')


def create_acount(request):
    return render(request, 'app/pages/create_acount.html')


def meus_formularios(request):
    return render(request, 'app/pages/meus-formularios.html')


def criar_formulario(request):
    return render(request, 'app/pages/criar-formulario.html')


def minha_conta(request):
    return render(request, 'app/pages/minha-conta.html')




