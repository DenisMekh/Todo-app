from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers.todos import router


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def on_startup():
    # Создаём таблицы при старте приложения
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

