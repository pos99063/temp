import traceback

from django.http import HttpRequest
from django.http import JsonResponse
from .models import Item
from apps.util.logger import log
from apps.user.models import RealUser
import json

def regist(request):
	try:
		if request.method != "POST":
			return JsonResponse(status=404, data={"response": "NOT FOUND"})

		requestBody = json.loads(str(request.body, encoding='UTF-8'))
		log.debug("%s",requestBody)

		item = Item(
			name=requestBody.get('name'),
			price=requestBody.get('price'),
			minRentDay=requestBody.get('minRentDay'),
			maxRentDay=requestBody.get('maxRentDay'),
			info=requestBody.get('info'),
			picture=requestBody.get('picture')
		)
		item.owner_id = int(requestBody.get('owner'))

		item.save()
	except Exception as Err:
		log.debug('%s', traceback.format_exc())
		return JsonResponse(status=400, data={"response": "bad request"})
		pass
	else:
		return JsonResponse(status=200, data={"response": "success"})


def list(request):
	try:
		records = Item.objects.all().order_by('-registDate')[:10]
		result = {}
		for i in range(0, len(records)):
			result[str(i)] = records[i].name
		log.debug("%s",result)
	except Exception as Err:
		log.debug('%s', traceback.format_tb(Err.__traceback__))
		return JsonResponse(status=400, data={"response": "bad request"})
	else:
		return JsonResponse(status=200, data=json.dumps(result), safe=False)

def search(request):
	try:
		records = Item.objects.all().order_by('-registDate')[:10]
		result = {}
		for i in range(0, len(records)):
			result[str(i)] = records[i].name
		log.debug("%s", result)
	except Exception as Err:
		log.debug('%s', traceback.format_tb(Err.__traceback__))
		return JsonResponse(status=400, data={"response": "bad request"})
	else:
		return JsonResponse(status=200, data=json.dumps(result), safe=False)

