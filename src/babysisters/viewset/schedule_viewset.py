from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from babysisters.models.schedule import Schedule
from babysisters.serializers.schedule_serializer import ScheduleSerializer, ScheduleListSerializer, \
    ScheduleStateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    @action(detail=False, url_path='schedule-available', methods=['get'], url_name='schedule_available')
    def schedule_available(self, request):
        queryset = Schedule.objects.exclude(state=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        return ScheduleSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
