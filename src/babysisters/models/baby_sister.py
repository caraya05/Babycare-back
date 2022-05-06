from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit


class BabySister(Audit):
    model_name = _('Baby sister')
    name: str = models.CharField(_('Name'), max_length=50, default='')
    last_name: str = models.CharField(_('Last name'), max_length=50, default='')
    document: str = models.CharField(_('Document'), max_length=20, default='')
    phone: str = models.CharField(_('Phone'), max_length=20, default='')
    date_b: date = models.DateField(_('Date birth'), null=True)

    class Meta:
        verbose_name = _('Baby sister')
        verbose_name_plural = _('Baby sisters')

    def __str__(self):
        return f'{self.name} {self.last_name}'

