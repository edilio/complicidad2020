from django.urls import reverse


def test_redirector_view(client):
    url = reverse('redirector')
    url += '?utm_source=google&utm_medium=cpc&utm_campaign=test&utm_term=test&utm_content=test'
    # from Italy should go to Italy
    response = client.get(url, HTTP_X_FORWARDED_FOR='103.47.156.0')
    assert response.status_code == 302
    assert response.url == 'https://www.amazon.it/dp/1685741274/?language=es_ES'
    # from US should go to US
    response = client.get(url, HTTP_X_FORWARDED_FOR='99.177.202.178')
    assert response.status_code == 302
    assert response.url == 'https://www.amazon.com/dp/1685741274/?language=es_ES'
