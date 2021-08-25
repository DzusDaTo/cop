from django.shortcuts import render
from .forms import TestForm


def testing(request):
    error = ''
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверно заполнена'
    form = TestForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'testing/testing.html', data)