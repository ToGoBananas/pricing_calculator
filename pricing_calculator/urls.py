from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('orders.urls')),
    url(r'^packages/$', views.PackagesResponseView.as_view(), name='package'),

    url(r'^$', views.CalculatorView.as_view(), name='calculator'),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
