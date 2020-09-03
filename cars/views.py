from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Car
from .forms import CarFrom

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
	form = CarFrom()
	if request.method == "POST":
		form = CarFrom(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'a new Car has been added ')
			return redirect('car-list')
	context = {
		'form': form
	}
	return render(request, 'create.html', context)


def car_update(request, car_id):
	car = Car.objects.get(id=car_id)
	form = CarFrom(instance=car)
	if request.method == "POST":
		form = CarFrom(request.POST,request.FILES, instance=car)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'the car has been updated')
			return redirect('car-list')
	#Complete Me
	context = {
		'form': form,
		'car': car,
	}
	return render(request, 'update.html', context, )


def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	messages.add_message(request, messages.INFO, 'the car has been deleted')
	return redirect('car-list')
