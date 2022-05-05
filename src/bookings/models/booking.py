from typing import Optional
from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit


class Booking(Audit):
    schedule: Optional = models.ForeignKey(to='babysisters.Schedule', verbose_name=_('Schedule'),
                                              on_delete=models.CASCADE)
    name: str = models.CharField(_('Name'), max_length=50, default='')
    document: str = models.CharField(_('Document'), max_length=20, default='')
    phone: str = models.CharField(_('Phone'), max_length=20, default='')
    direction: str = models.CharField(_('Direction'), max_length=100, default='')


    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')

    def __str__(self):
        return f'{self.name} {self.document}'
