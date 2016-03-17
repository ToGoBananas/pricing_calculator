from django.shortcuts import render_to_response, render
from django.views.generic import View
from .models import Package, Datacenter


class CalculatorView(View):

    def get(self, request, *args, **kwargs):
        packages = Package.objects.filter(status='active')
        packages_names = [x.get('name') for x in packages.values('name').distinct()]
        packages = packages.filter(name=packages_names[0])
        return render(request, 'pricing_calculator.html', {
            'packages': packages,
            'packages_names': packages_names
        })


class PackagesResponseView(View):

    template_name = 'packages.html'

    def get(self, request, *args, **kwargs):
        package_name = request.GET['package_name']
        packages = Package.objects.filter(name=package_name, status='active')
        return render_to_response('packages.html', {
            'packages': packages,
        })
