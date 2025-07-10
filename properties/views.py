#property view that caches the response in Redis for 1 hour

from .utils import get_all_properties
from django.views.decorators.cache import cache_page
from django.http import JsonResponse

def property_list(request):
    properties = get_all_properties()
    return JsonResponse({
        "data": list(properties)
        })


