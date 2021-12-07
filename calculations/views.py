from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'calculations/index.html', )


def multiplication(request):
    return render(request, 'calculations/multiplication.html', )
