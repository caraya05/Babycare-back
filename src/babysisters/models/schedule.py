from datetime import date, time

from typing import Optional
from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit


class Schedule(Audit):
    day: date = models.DateField(_('Day'))
    start_hour: time = models.TimeField(_('Start hour'))
    end_hour: time = models.TimeField(_('End hour'))
    baby_sister: Optional = models.ForeignKey(to='babysisters.BabySister', verbose_name=_('Baby sister'),
                                              on_delete=models.CASCADE)
    state: bool = models.BooleanField(_('State'), default=True)

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')

    def __str__(self):
        return f'{self.baby_sister} {self.state}'
