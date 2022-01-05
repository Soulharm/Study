from django.shortcuts import render

from calculations.functions import testmultdiv
from django.shortcuts import render


def index(request):
    return render(request, 'calculations/index.html', )

def count(request):
    pass

def multiplication(request):
    # Создаём массивы примеров и правильных решений для рендеринга
    examples, results = testmultdiv(5)
    dict_result = dict(zip(examples, results))
    result = {'result': dict_result}
    return render(request, 'calculations/testyourself.html', context=result)


def division(request):
    return render(request, 'calculations/testyourself.html', )
