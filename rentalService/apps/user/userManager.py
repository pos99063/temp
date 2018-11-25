import traceback
import json

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out,	user_login_failed

from .models import RealUser
from apps.util.logger import log



def userSignIn(request):
	try:
		if request.method != "POST":
			return HttpResponse(status=404)
		print(request.body)
		requestBody = json.loads(str(request.body, encoding='UTF-8'))
		log.debug("%s",requestBody)

		user = RealUser(
			userId=requestBody.get('userId'),
			name=requestBody.get('userName')
		)
		user.set_password(requestBody.get('passWd'))
		user.save()

	except Exception as Err:
		print('%s', traceback.format_exc())
		return HttpResponse(status=400)
	else:
		return HttpResponse("success")


def userLogIn(request):
	state = "Please log in below..."
	userId = password = ''
	if request.method != "POST":
		return HttpResponse(status=404)
	requestBody = json.loads(str(request.body, encoding='UTF-8'))
	userId = requestBody['userId']
	passWd = requestBody['passWd']
	print("%s %s"%(userId,passWd))
	user = authenticate(userId=userId,password=passWd)
	print(user)
	if user is not None:
		if user.is_active:
			user_logged_in.send(
				sender = RealUser,
				request = request,
				user = user,
			)
			request.session['userId'] = userId
			login(request, user)
			state = "Login_Success"
			print (state)
			return HttpResponse('Success')

		else:
			state = "Your account is not active, please contact the site admin"
			print (state)
			return HttpResponse('Not_Active', status=403)
	else:
		user_login_failed.send(
			sender = RealUser,
			request = request,
			credentials = {
				'email':userId
			},
		)
		state = "Your username and/or password were incorrect"
		print (state)
		return HttpResponse('Not_Correct 1')


def userLogOut(request):
	if request.user.is_authenticated:
		user_logged_out.send(
			sender = RealUser,
			request = request,
			user = request.user,
		)
		logout(request)
		return HttpResponse('Success')
	else:
		return HttpResponse(status=400)

def userSignOut(request):
	return HttpResponse('Not Implemented Yet', stauts=500)

