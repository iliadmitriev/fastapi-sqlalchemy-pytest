import pytest
from starlette import status


@pytest.mark.asyncio
async def test_view_health_check_200_ok(get_client):
    res = await get_client.get('/')
    assert res.status_code == status.HTTP_200_OK
