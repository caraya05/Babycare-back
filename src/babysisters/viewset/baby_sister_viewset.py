from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from babysisters.models.baby_sister import BabySister
from babysisters.serializers.baby_sister_serializer import BabySisterSerializer, BabySisterListSerializer


class BabySisterViewSet(viewsets.ModelViewSet):
    queryset = BabySister.objects.all()
    serializer_class = BabySisterSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BabySisterListSerializer
        return BabySisterSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
