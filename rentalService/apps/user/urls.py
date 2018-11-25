from django.conf.urls import url, include

from apps.user import views
from . import userManager
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', userManager.userLogIn),
    url(r'^logout/', userManager.userLogOut),
    url(r'^signin/',userManager.userSignIn),
    url(r'^signout/',userManager.userSignOut)
]