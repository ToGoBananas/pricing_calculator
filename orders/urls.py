from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^order/$', views.OrderView.as_view(), name='order'),
]
