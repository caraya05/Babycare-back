from django.contrib import admin
from loducode_utils.admin import AuditAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from babysisters.models.schedule import Schedule


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule
        fields = '__all__'


@admin.register(Schedule)
class ScheduleAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = ScheduleResource
    list_display = ('baby_sister', 'day', 'start_hour', 'end_hour', 'state',)
    list_display_links = ('baby_sister', 'day', 'start_hour', 'end_hour', 'state',)
    search_fields = ('baby_sister__name', 'baby_sister__last_name', 'state', 'baby_sister__phone',)
    list_filter = ('state',)
    raw_id_fields = ('baby_sister',)
