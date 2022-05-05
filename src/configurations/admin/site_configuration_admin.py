from django.contrib import admin

from solo.admin import SingletonModelAdmin
from configurations.models.site_configuration import SiteConfigurationM

admin.site.register(SiteConfigurationM, SingletonModelAdmin)
