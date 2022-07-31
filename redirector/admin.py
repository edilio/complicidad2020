from django.contrib import admin

from .models import Marketing


@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    list_display = ('utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'affiliate_id',
                    'affiliate_cid', 'gclid', 'gacid', 'msclkid', 'users_ip', 'country')
    list_filter = ('country',)
