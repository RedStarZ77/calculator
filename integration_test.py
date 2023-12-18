from main import calc


def test_root_get():
    res = calc(2,5,"add")
    assert res == 7
