from loducode_utils.serializers import AuditSerializer

from babysisters.models.schedule import Schedule
from rest_framework import serializers


class ScheduleSerializer(AuditSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'start_hour', 'end_hour', 'baby_sister', 'state',)


class ScheduleListSerializer(AuditSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'start_hour', 'end_hour', 'baby_sister', 'state')


class ScheduleCreateSerializer(AuditSerializer):
    # def validate(self,instance):
    #   if instance.date_b

    class Meta:
        model = Schedule
        fields = ('id', 'day', 'start_hour', 'end_hour', 'baby_sister', 'state',)


class ScheduleStateSerializer(AuditSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'start_hour', 'end_hour', 'baby_sister',)
