from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import itemManager


urlpatterns = [
    url(r'^test', views.index),
    url(r'^regist/', itemManager.regist),
    url(r'^list/', itemManager.list)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)