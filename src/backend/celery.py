from __future__ import absolute_import, unicode_literals  # pylint:disable=C0114
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
app = Celery('backend')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)
