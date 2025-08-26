from django.shortcuts import render
from django.http import JsonResponse
from .models import Property
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    )

    response_data = {
        'data': list(properties)
    }

    return JsonResponse(response_data)
