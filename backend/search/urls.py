from django.urls import path

from .views import (
    get_furniture_list,
    get_furniture_detail,
    get_locations,
)

urlpatterns = [
    path('furniture/', get_furniture_list, name='furniture-list'),
    path('furniture/<int:furniture_id>/', get_furniture_detail, name='furniture-detail'),
    path('locations/', get_locations, name='location-list'),
]
