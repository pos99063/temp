import traceback

from django.http import HttpRequest
from django.http import JsonResponse
from .models import User
from apps.util.logger import log
import json

def signin(request):
	try:
		if request.method == "POST":
			pass
		else:
			return JsonResponse(status=404, data={"response": "NOT FOUND"})

		requestBody = json.loads(str(request.body, encoding='UTF-8'))
		log.debug("%s",requestBody)

		user = User(
			#name=requestBody.get('name'),
			postCode=requestBody.get('postCode'),
			address=requestBody.get('address'),
			phone=requestBody.get('phone'),
		)
		user.save()
	except Exception as Err:
		log.debug('%s', traceback.format_exc())
		return JsonResponse(status=400, data={"response": "bad request"})
		pass
	else:
		return JsonResponse(status=200, data={"response": "success"})
