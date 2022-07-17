from main.models import Bid
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('dashboard'))
	return render(request, 'index.html')


def sign_in(request):
	user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
	if user is not None:
		print('dash')
		return HttpResponseRedirect(reverse('dashboard'))
	else:
		return HttpResponseRedirect(reverse('index'))


def sign_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def dashboard(request):
	if not request.user.is_anonymous:
		return HttpResponseRedirect(reverse('index'))

	bids = Bid.objects.all().order_by('-date')
	return render(request, 'dashboard.html', {'bids': bids})


def remove(request, id):
	Bid.objects.get(pk = id).delete()
	return HttpResponseRedirect(reverse('dashboard'))