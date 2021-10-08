import asyncio

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient


@pytest.fixture(scope='session')
async def get_app():
    from main import app
    async with LifespanManager(app):
        yield app


@pytest.fixture(scope='session')
async def get_client(get_app):
    async with AsyncClient(app=get_app, base_url="http://testserver") as client:
        yield client


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
