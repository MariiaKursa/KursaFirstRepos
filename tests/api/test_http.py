import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/serhii_butenko')
    body = r.json()
    headers = r.headers
    
    
    assert r.status_code == 404
