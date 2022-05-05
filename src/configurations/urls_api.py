from django.urls import include, path
from rest_framework import routers

from configurations.viewset.city_viewset import CityViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = [
    path('', include(router.urls)),
]
