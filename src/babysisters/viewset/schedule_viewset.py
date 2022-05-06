from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.translation import gettext_lazy as _

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
        queryset = Schedule.objects.exclude(state=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        return ScheduleSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


EXAMPLE = (' ** { '
           '"day": "dd/mm/yyyy", '
           '"start_hour": "hh:mm:ss", '
           '"end_hour": "hh:mm:ss", '
           '"baby_sister": "UUID", '
           '"state": True, '
           ' } **')

ScheduleViewSet.__doc__ = """
list:
   {LIST}
create:
    {CREATE}
retrieve:
   {RETRIEVE} 
schedule_available:
    {SCHEDULE_AVAILABLE}
update:
    {UPDATE}
partial_update:
    {PARTIAL_UPDATE}
destroy:
    {DESTROY}
""".format(
    LIST=_("List of all schedules registered in the system."),
    CREATE=_("Create a schedule data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific schedule."),
    SCHEDULE_AVAILABLE=_("List of all schedules available registered in the system."),
    UPDATE=_("Update a schedule data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a schedule data.") + ' ** { "name": "example name" } **',
    DESTROY=_("Destroy a schedule data."),
)
