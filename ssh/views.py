import json
from main.models import Bid, Channel
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


def source(request):
	channels = Channel.objects.all()
	channel_list = list()
	for channel in channels:
		channel_list.append(channel.name)

	return JsonResponse(channel_list, safe = False)