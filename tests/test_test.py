import pytest
from blacksheep.testing import TestClient


@pytest.mark.asyncio
async def test_create_and_get_todo(test_client: TestClient) -> None:
    response = await test_client.get("/")

    assert response is not None
