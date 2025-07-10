from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connetion

def get_all_properties():
    try:
        conn = get_redis_connection("default")
        info = conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total = hits + misses

        hit_ratio = (hit / total) if total > 0 else 0.0

        metrics = {
                "hits": hits,
                "misses": misses,
                "hit_ratio": round(hit_ratio, 4),
                }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics

    exception Exception as e:
        logger.error(f"Failed to get Redis Cache metrics: {e}")
        return {
                "hits": 0,
                "misses": 0,
                "hit_ratio": 0,
                "error": str{e}}

    properties = cache.get('all_properties')

    if properties is None:
        print("Fetching from DB...")

        #serialize so it can be stored in Redis
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, timeout=3600)
    else:
        print("Fetching from DB...")

    return properties
