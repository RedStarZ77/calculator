import requests


base_url = 'http://localhost:3001/'


def test_root_get():
    res = requests.get(base_url+'?num1=2&num2=2&operation=add').json()
    assert 'result' in res
