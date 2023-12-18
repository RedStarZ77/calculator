import pytest
from uuid import uuid4
from time import sleep
from datetime import datetime
from main import root
import json
import asyncio
from fastapi import Query


def test_root_get():
    res = asyncio.run(root())
    assert 'num1' in res
    assert 'num2' in res
    assert 'result' in res
