#property view that caches the response in Redis for 15 minutes

from django.shortcuts import render
from .models import Property
from rest_framework.decorators import cache_page
from django.http import JsonResponse

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values
    return JsonResponse(list(properties))


