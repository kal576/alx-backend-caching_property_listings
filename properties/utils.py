from django.core.cache import cache
from .models import Property

def get_all_properties():
    properties = cache.get('all_properties')

    if properties is None:
        print("Fetching from DB...")

        #serialize so it can be stored in Redis
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, timeout=3600)
    else:
        print("Fetching from DB...")

    return properties
