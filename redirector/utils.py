import logging

from ip3country import CountryLookup

logger = logging.getLogger('complicidad')


def get_ip(req):
    ip = req.META.get('HTTP_X_FORWARDED_FOR', None)
    remote_ip = req.META.get('REMOTE_ADDR', None)
    logger.info(f'HTTP_X_FORWARDED_FOR: {ip}')
    logger.info(f'REMOTE_ADDR: {remote_ip}')
    if ip:
        ip = ip.split(',')[-1].strip()
    # forwarded proxy fix for proxy passing setups
    if (not ip or ip == '127.0.0.1') and 'REMOTE_ADDR' in req.META:
        ip = remote_ip
    return ip


def get_country(ip: str) -> str | None:
    lookup = CountryLookup()
    return lookup.lookupStr(ip)


COUNTRY_MAPPING = {
    'US': 'amazon.com',
    'CA': 'amazon.ca',
    'UK': 'amazon.co.uk',
    'DE': 'amazon.de',
    'FR': 'amazon.fr',
    'IT': 'amazon.it',
    'ES': 'amazon.es',
    'JP': 'amazon.co.jp',
    'CN': 'amazon.cn',
    'BR': 'amazon.com.br',
    'MX': 'amazon.com.mx',
    'AU': 'amazon.com.au',
    'IN': 'amazon.in',
    'AE': 'amazon.ae',
    'PL': 'amazon.pl',
}


def gen_destination_url(country: str):
    domain = COUNTRY_MAPPING.get(country) or 'amazon.com'
    return f'https://www.{domain}/dp/1685741274/?language=es_ES'
