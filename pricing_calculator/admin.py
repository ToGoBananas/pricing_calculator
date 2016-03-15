from django.contrib import admin
from .models import Package, Datacenter, Feature, VirtualMachine


class PackageAdmin(admin.ModelAdmin):
    filter_horizontal = ('features', 'virtual_machines')
    list_display = ('name', 'datacenter', 'total_price')


class DatacenterAdmin(admin.ModelAdmin):
    filter_horizontal = ('available_machines', )


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class VirtualMachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Package, PackageAdmin)
admin.site.register(Datacenter, DatacenterAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(VirtualMachine, VirtualMachineAdmin)

