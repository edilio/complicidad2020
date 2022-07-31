from django.db import models

from django_countries.fields import CountryField


class Marketing(models.Model):
    utm_source = models.CharField(max_length=255, null=True, blank=True)
    utm_medium = models.CharField(max_length=255, null=True, blank=True)
    utm_campaign = models.CharField(max_length=255, null=True, blank=True)
    utm_term = models.CharField(max_length=255, null=True, blank=True)
    utm_content = models.CharField(max_length=255, null=True, blank=True)
    affiliate_id = models.CharField(max_length=255, null=True, blank=True)
    affiliate_cid = models.CharField(max_length=255, null=True, blank=True)
    gclid = models.CharField(max_length=255, null=True, blank=True)
    gacid = models.CharField(max_length=255, null=True, blank=True)
    msclkid = models.CharField(max_length=255, null=True, blank=True)

    users_ip = models.GenericIPAddressField(max_length=255, null=True, blank=True)
    country = CountryField(null=True, blank=True)
