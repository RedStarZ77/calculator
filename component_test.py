import requests


base_url = 'http://localhost:3001/'


def test_root_get():
    res = requests.get(base_url+'?num1=2&num2=2&operation=add')
    assert '{"num1":2.0,"num2":2.0,"result":4.0}' in res.text
