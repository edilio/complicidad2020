from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def buy(request):
    return render(request, 'website/comprar.html')


def about(request):
    return render(request, 'website/sobre-la-autora.html')


def contact_us(request):
    return render(request, 'website/contactanos.html')
