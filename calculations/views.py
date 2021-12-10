from django.shortcuts import render

from calculations.functions import testmultdiv


def index(request):
    return render(request, 'calculations/index.html', )


def multiplication(request):
    # Создаём массивы примеров и правильных решений для рендеринга
    examples, results = testmultdiv(5)
    result = {"examples": examples,
              'results': results}
    return render(request, 'calculations/testyourself.html', context=result)


def division(request):
    return render(request, 'calculations/testyourself.html', )
