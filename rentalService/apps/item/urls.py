from django.conf.urls import url, include
from . import views
from . import itemManager


urlpatterns = [
    url(r'^test', views.index),
    url(r'^regist/', itemManager.regist),
    url(r'^list/', itemManager.list)
]