from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('packages', )
    fields = ('email', 'packages', )
    list_display = ('email', 'created')

admin.site.register(Order, OrderAdmin)
