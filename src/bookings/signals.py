from django.db.models.signals import post_save
from django.dispatch import receiver

from bookings.models.booking import Booking
from babysisters.models.schedule import Schedule


@receiver(post_save, sender=Booking, weak=False)
def update_state_schedule(
        sender, instance, created, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    schedule = Schedule.objects.filter(id=instance.schedule.id).first()
    schedule.state = False
    print('----------', schedule)
    schedule.save()
