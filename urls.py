
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.AddIPAddress.as_view()),
    url(r'^get$', views.GetIPAddresses.as_view()),
]
