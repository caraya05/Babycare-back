from django.contrib import admin
from loducode_utils.admin import AuditAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from bookings.models.booking import Booking


class BookingResource(resources.ModelResource):
    class Meta:
        model = Booking
        fields = '__all__'


@admin.register(Booking)
class BookingAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = BookingResource
    list_display = ('schedule', 'name', 'document', 'phone', 'direction',)
    list_display_links = ('schedule', 'name', 'document', 'phone', 'direction',)
    search_fields = ('name', 'document', 'phone',)
    raw_id_fields = ('schedule',)
