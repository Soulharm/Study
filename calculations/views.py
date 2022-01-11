from django.shortcuts import render

from calculations.functions import test_mult_div
from django.shortcuts import render


def index(request):
    return render(request, 'calculations/index.html', )


def multiplication(request):
    # Создаём массивы примеров и правильных решений для рендеринга
    examples, results = test_mult_div(5, 'mult')
    dict_result = dict(zip(examples, results))
    result = {'result': dict_result}
    return render(request, 'calculations/testyourself.html', context=result)


def division(request):
    # Создаём массивы примеров и правильных решений для рендеринга
    examples, results = test_mult_div(5, 'div')
    dict_result = dict(zip(examples, results))
    result = {'result': dict_result}
    return render(request, 'calculations/testyourself.html', context=result)
