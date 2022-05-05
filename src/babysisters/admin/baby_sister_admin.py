from django.contrib import admin
from loducode_utils.admin import AuditAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from babysisters.models.baby_sister import BabySister


class BabySisterResource(resources.ModelResource):
    class Meta:
        model = BabySister
        fields = '__all__'


@admin.register(BabySister)
class BabySisterAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = BabySisterResource
    list_display = ('name', 'last_name', 'document', 'phone', 'date_b',)
    list_display_links = ('name', 'last_name', 'document', 'phone', 'date_b',)
    search_fields = ('name', 'last_name', 'document', 'phone',)
