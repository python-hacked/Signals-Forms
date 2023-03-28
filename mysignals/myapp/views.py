from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel
from .forms import MyModelForm
from django.contrib import messages

def index(request):
    models = MyModel.objects.all()
    return render(request, 'index.html', {'models': models})

def create(request):
    form = MyModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.success(request, 'Model created successfully.')
        return redirect('/')
    return render(request, 'form.html', {'form': form})

def update(request, id):
    model = get_object_or_404(MyModel, id=id)
    form = MyModelForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        # messages.success(request, 'Model updated successfully.')
        return redirect('/')
    return render(request, 'form.html', {'form': form})

def delete(request, id):
    model = get_object_or_404(MyModel, id=id)
    if request.method == 'POST':
        model.delete()
        # messages.success(request, 'Model deleted successfully.')
        return redirect('/')    
    return render(request, 'confirm_delete.html', {'model': model})
