# ./tests/conftest.py

import asyncio

import pytest
import pytest_asyncio
from blacksheep.testing import TestClient

from test_blacksheep_pytest.main import app


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def api():
    await app.start()
    yield app
    await app.stop()


@pytest.fixture(scope="session")
async def test_client(api):
    return TestClient(api)