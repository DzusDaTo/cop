from django.shortcuts import render


def testing(request):
    return render(request, 'testing/testing.html')
