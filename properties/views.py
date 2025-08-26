from django.shortcuts import render
from django.http import JsonResponse
from .models import Property
from django.views.decorators.cache import cache_page
from .utils import getallproperties

@cache_page(60 * 15)
def property_list(request):
    properties_queryset = getallproperties()
    return JsonResponse({'data': list(properties_queryset)})
