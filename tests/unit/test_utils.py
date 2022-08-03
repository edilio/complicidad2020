from redirector.utils import gen_destination_url, get_country, get_ip, valid_ipv4


def test_valid_ipv4():
    assert valid_ipv4('103.47.156.1')
    assert not valid_ipv4('1030.47.156.1')
    assert not valid_ipv4('2a03:2880:21ff:2::face:b00c')
    assert not valid_ipv4('2a09:8280:1::59c0')


def test_get_ip():
    class FakeRequest:
        def __init__(self, attrib: str, ip: str):
            self.META = {attrib: ip}

        def add(self, attrib: str, ip: str):
            self.META[attrib] = ip

    req = FakeRequest('HTTP_X_FORWARDED_FOR', '103.47.156.1')
    assert get_ip(req) == '103.47.156.1'
    # forwarded proxy fix for proxy passing setups
    req = FakeRequest('REMOTE_ADDR', '103.47.156.1')
    assert get_ip(req) == '103.47.156.1'
    # real sample
    req = FakeRequest('HTTP_X_FORWARDED_FOR', '2600:1700:16d0:7620:f97b:13db:a960:889, 2a09:8280:1::59c0')
    req.add('REMOTE_ADDR', '66.225.243.53')
    assert get_ip(req) == '66.225.243.53'


def test_get_country():
    assert get_country('99.177.202.178') == 'US'
    assert get_country('123.45.67.8') == 'KR'


def test_gen_destination_url():
    assert gen_destination_url('UK') == 'https://www.amazon.co.uk/dp/1685741274/?language=es_ES'
    # test a country not in the list should go to amazon.com
    assert gen_destination_url('AR') == 'https://www.amazon.com/dp/1685741274/?language=es_ES'
