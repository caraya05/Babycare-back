from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from bookings.models.booking import Booking
from bookings.serializers.booking_serializer import BookingSerializer, BookingListSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BookingListSerializer
        return BookingSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
