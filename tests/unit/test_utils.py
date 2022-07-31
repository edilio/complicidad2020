from redirector.utils import gen_destination_url, get_country, get_ip


def test_get_ip():
    class FakeRequest:
        def __init__(self, attrib: str, ip: str):
            self.META = {attrib: ip}

    req = FakeRequest('HTTP_X_FORWARDED_FOR', '103.47.156.1')
    assert get_ip(req) == '103.47.156.1'
    # forwarded proxy fix for proxy passing setups
    req = FakeRequest('REMOTE_ADDR', '103.47.156.1')
    assert get_ip(req) == '103.47.156.1'


def test_get_country():
    assert get_country('99.177.202.178') == 'US'
    assert get_country('123.45.67.8') == 'KR'


def test_gen_destination_url():
    assert gen_destination_url('UK') == 'https://www.amazon.co.uk/dp/1685741274/?language=es_ES'
    # test a country not in the list should go to amazon.com
    assert gen_destination_url('AR') == 'https://www.amazon.com/dp/1685741274/?language=es_ES'
