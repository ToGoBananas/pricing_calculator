from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('datacenters', 'features')
    fields = ('__all__', )

admin.site.register(Order, OrderAdmin)