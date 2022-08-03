import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

from .models import Marketing


class CustomDateFieldListFilter(admin.DateFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        now = timezone.now()
        if timezone.is_aware(now):
            now = timezone.localtime(now)
        if isinstance(field, models.DateTimeField):
            today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        else:       # field is a models.DateField
            today = now.date()
        yesterday = today - datetime.timedelta(days=1)
        last_month = today.month - 1 if today.month > 1 else 12
        first_day_last_month = today.replace(month=last_month, day=1)
        last_year = today.replace(year=today.year - 1, month=1, day=1)

        super().__init__(field, request, params, model, model_admin, field_path)
        self.links = list(self.links)
        self.links.insert(1,
                          ('Yesterday', {
                              self.lookup_kwarg_since: str(yesterday),
                              self.lookup_kwarg_until: str(today),
                          }), )
        self.links.extend([('Last month', {
                              self.lookup_kwarg_since: str(first_day_last_month),
                              self.lookup_kwarg_until: str(today.replace(day=1)),
                          }), ('Last year', {
                              self.lookup_kwarg_since: str(last_year),
                              self.lookup_kwarg_until: str(today.replace(month=1, day=1)),
                          })])
        self.links = tuple(self.links)


@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    list_display = ('utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'affiliate_id',
                    'affiliate_cid', 'gclid', 'gacid', 'msclkid', 'users_ip', 'country', 'created_at')
    list_filter = (('created_at', CustomDateFieldListFilter), 'country')
