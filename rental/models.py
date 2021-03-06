from django.db import models
from shelf.models import BookItem
from django.conf import settings
from django.db.models import Q

# from datetime import datetime.now as now  # nie wspiera stref czasowych
# from django.utils.timezone import now   # wspiera strefy czasowe OotB (Out of the Box)


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    what = models.ForeignKey(BookItem,
                             limit_choices_to=Q(rental__returned__isnull=False) | Q(rental__isnull=True)
    )
    when = models.DateTimeField(auto_now_add=True)  # nie można zmienić ręcznie
    returned = models.DateTimeField(null=True, blank=True)  # domyślnie pojawia się w formularzu

    def __str__(self):
        return "{who.username} rent: {what.edition.book.title} [{what.pk}]" \
               " at {when}".format(who=self.who,
                                   what=self.what,
                                   when=self.when)

    class Meta:
        permissions = (
            ('can_rent', 'Can rent a book'),
        )