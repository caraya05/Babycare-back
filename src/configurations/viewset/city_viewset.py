from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework import permissions
from loducode_utils.models.city import City
from loducode_utils.serializers import CitySerializer


class CityViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['name']
    filter_fields = {
        'name': ['exact', 'icontains'],
        'state': ['exact'],
    }
