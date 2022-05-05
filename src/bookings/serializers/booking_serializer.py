from loducode_utils.serializers import AuditSerializer

from bookings.models.booking import Booking
from rest_framework import serializers


class BookingSerializer(AuditSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'schedule', 'name', 'document', 'phone', 'direction',)


class BookingListSerializer(AuditSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'schedule', 'name', 'document', 'phone', 'direction',)


class BookingCreateSerializer(AuditSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'schedule', 'name', 'document', 'phone', 'direction',)
