from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils.translation import gettext_lazy as _

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


EXAMPLE = (' ** { '
           '"schedule": UUID, '
           '"name": string, '
           '"document": "string", '
           '"phone": "string", '
           '"direction": "string", '
           ' } **')

BookingViewSet.__doc__ = """
list:
   {LIST}
create:
    {CREATE}
retrieve:
   {RETRIEVE} 
update:
    {UPDATE}
partial_update:
    {PARTIAL_UPDATE}
destroy:
    {DESTROY}
""".format(
    LIST=_("List of all bookings registered in the system."),
    CREATE=_("Create a booking data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific booking."),
    UPDATE=_("Update a booking data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a booking data.") + ' ** { "day": "example day" } **',
    DESTROY=_("Destroy a booking data."),
)
