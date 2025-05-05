from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK
)

from .models import Furniture, Location


@api_view(['GET'])
def get_locations(request):
    locations = Location.objects.all()
    result = []
    for loc in locations:
        result.append({
            'id': loc.id,
            'region': loc.region,
            'city': loc.city,
            'street': loc.street,
            'house': loc.house
        })
    return Response({'items': result}, status=HTTP_200_OK)


@api_view(['GET'])
def get_furniture_list(request):
    furniture_items = Furniture.objects.select_related('location').all().order_by('-created_at')
    result = []
    for item in furniture_items:
        result.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'width_cm': item.width_cm,
            'height_cm': item.height_cm,
            'depth_cm': item.depth_cm,
            'color': item.color,
            'photo_path': item.photo_path.url if item.photo_path else None,
            'created_at': item.created_at.isoformat(),
            'location': {
                'region': item.location.region,
                'city': item.location.city,
                'street': item.location.street,
                'house': item.location.house,
            }
        })
    return Response({'items': result}, status=HTTP_200_OK)


@api_view(['GET'])
def get_furniture_detail(request, furniture_id):
    item = get_object_or_404(Furniture.objects.select_related('location'), id=furniture_id)
    data = {
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'width_cm': item.width_cm,
        'height_cm': item.height_cm,
        'depth_cm': item.depth_cm,
        'color': item.color,
        'photo_path': item.photo_path.url if item.photo_path else None,
        'created_at': item.created_at.isoformat(),
        'location': {
            'region': item.location.region,
            'city': item.location.city,
            'street': item.location.street,
            'house': item.location.house,
        }
    }
    return Response(data, status=HTTP_200_OK)
