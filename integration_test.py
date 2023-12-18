from main import root
import asyncio


def test_root_get():
    res = asyncio.run(root())
    assert 'num1' in res
    assert 'num2' in res
    assert 'result' in res
