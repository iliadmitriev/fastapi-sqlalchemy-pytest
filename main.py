import sqlalchemy as sa
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from starlette.requests import Request

app = FastAPI()
DATABASE_URL = 'sqlite+aiosqlite://?cache=shared'


@app.on_event('startup')
async def startup_event():
    engine = create_async_engine(DATABASE_URL, future=True)
    app.state.session = AsyncSession(engine, expire_on_commit=False)
    app.state.engine = engine


@app.on_event('shutdown')
async def shutdown_event():
    await app.state.session.close()


@app.get('/', name="home")
async def get_home(request: Request):
    res = await request.app.state.session.execute(sa.text('SELECT 1'))
    # after this line coverage breaks
    row = res.first()
    assert str(row[0]) == '1'
    return {"message": "OK"}
