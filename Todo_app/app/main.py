import sys
import asyncio

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from app.crud import create_todo, get_todos
from app.database import engine
from app.models import Base


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def test_crud():
    # Создаём таблицы
    await init_db()

    # Создаём новую задачу
    new_todo = await create_todo("Сделать домашку")
    print("Создано:", new_todo.id, new_todo.text, new_todo.status)

    # Получаем все задачи
    todos = await get_todos()
    print("Все задачи:")
    for todo in todos:
        print(todo.id, todo.text, todo.status)

if __name__ == "__main__":
    asyncio.run(test_crud())
