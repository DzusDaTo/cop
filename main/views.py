from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def index_sch(request):
    return render(request, 'main/index_sch.html')