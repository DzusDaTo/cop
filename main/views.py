from django.shortcuts import render, redirect
from .forms import ShipmentForm
from .models import Shipment


def index(request):
    return render(request, 'main/index.html')


def index_sch(request):
    error = ''
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ShipmentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index_sch.html', data)
