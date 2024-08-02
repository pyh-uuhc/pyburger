from django.shortcuts import render

from burgers.models import Burger


def main(request):
    return render(request, 'main.html')


def burger_list(request):
    burgers = Burger.objects.all()
    print('전체 햄버거 목록:', burgers)

    context = {
        'burgers': burgers,
    }
    return render(request, 'burger_list.html', context)


def burger_search(request):
    return render(request, 'burger_search.html')
