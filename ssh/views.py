import json
from main.models import Bid
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def ping(request):
	return JsonResponse('Ready to receive', safe = False)


@csrf_exempt
def create(request):
	data = json.loads(request.body)
	bid = Bid()
	bid.name = data['name']
	bid.phone = data['phone']
	bid.language = data['language']
	bid.source = data['source']
	bid.product = data['product']
	bid.save()

	return JsonResponse(200, safe = False)