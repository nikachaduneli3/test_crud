from django.shortcuts import render, redirect
from .models import Test
from .forms import TestForm

def home(request):
    records = Test.objects.all()
    return render(request, 'home.html', context={'recs': records})

def create(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', context={'form': TestForm()})

def detail_rec(request, pk):
    rec = Test.objects.get(id=pk)
    return render(request, 'detail_rec.html', context={'rec': rec})

def delete_rec(request, pk):
    Test.objects.get(id=pk).delete() 
    return redirect('home')

def update_rec(request, pk):
    rec = Test.objects.get(id=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('detail_rec', pk=pk)
    return render(request, 'create.html', context={'form': TestForm(instance=rec)})
