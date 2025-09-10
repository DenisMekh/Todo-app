from app.database import engine
import asyncio

async def test_connection():
    async with engine.begin() as conn:
        await conn.run_sync(lambda _: print("Connected to the database"))

asyncio.run(test_connection())
