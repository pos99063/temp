from django.conf.urls import url, include

from apps.user import views
from apps.user import validation
from . import userManager
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', validation.login),
    url(r'^signin/',userManager.signin)
]