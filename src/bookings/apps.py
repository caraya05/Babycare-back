from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BookingsConfig(AppConfig):
    name = 'bookings'
    verbose_name = _('Bookings')

    def ready(self):
        import bookings.signals  # pylint: disable=C0415 W0611
