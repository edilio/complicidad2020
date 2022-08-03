import logging

from ip3country import CountryLookup

logger = logging.getLogger('complicidad')


def valid_ipv4(address: str) -> bool:
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes if 0 <= int(b) <= 255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:  # noqa
        return False


def get_ip(req):
    ip = req.META.get('HTTP_X_FORWARDED_FOR', None)
    remote_ip = req.META.get('REMOTE_ADDR', None)
    logger.info(f'HTTP_X_FORWARDED_FOR: {ip}')
    logger.info(f'REMOTE_ADDR: {remote_ip}')
    if ip:
        ip = ip.split(',')[-1].strip()
    if valid_ipv4(ip):
        return ip
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
