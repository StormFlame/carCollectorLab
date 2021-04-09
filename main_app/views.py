from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Mod
from .forms import DrivenForm

# Create your views here.
def home(request):
    return redirect('/cars/')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render (request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    mods_car_doesnt_have = Mod.objects.exclude(id__in = car.mods.all().values_list('id'))
    driven_form = DrivenForm()
    return render (request, 'cars/detail.html', {'car': car, 'driven_form': driven_form, 'mods': mods_car_doesnt_have})

def add_drive(request, car_id):
    form = DrivenForm(request.POST)

    if form.is_valid():
        new_drive = form.save(commit=False)
        new_drive.car_id = car_id
        new_drive.save()
    return redirect('detail', car_id=car_id)

def assoc_mod(request, car_id, mod_id):
  Car.objects.get(id=car_id).mods.add(mod_id)
  return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = ['name', 'make', 'model', 'year', 'color']

class CarUpdate(UpdateView):
  model = Car
  fields = ['name', 'color']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'