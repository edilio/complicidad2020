import logging

from django.shortcuts import redirect

from .utils import gen_destination_url, get_ip, get_country
from .models import Marketing

logger = logging.getLogger(__name__)


def gen_marketing_data(req):
    ret = {}
    for field in ('utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
                  'affiliate_id', 'affiliate_cid', 'gclid', 'gacid', 'msclkid'):
        if field in req.GET:
            ret[field] = req.GET[field]
    return ret


def redirector(request):
    ip = get_ip(request)
    country = get_country(ip)
    try:
        Marketing.objects.create(users_ip=ip, country=country, **gen_marketing_data(request))
    except Exception as e:
        logger.error(e)
    url = gen_destination_url(country)
    return redirect(url)
