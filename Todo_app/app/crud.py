from app.models import Todo
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


async def create_todo(text: str, db: AsyncSession, status: bool = False) -> Todo:
    """
    Создает новую задачу

    Args:
        text (str): текст задачи
        status (bool): статус задачи

    Returns:
        Todo: созданная задача
    """
    
    todo = Todo(text=text, status=status)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def get_todos(db: AsyncSession) -> List[Todo]:
    """
    Получает список всех задач

    Returns:
        List[Todo]: список задач
    """
    
    result = await db.execute(select(Todo))
    todos = result.scalars().all()
    return todos
    
    
async def update_todo(id: int, db: AsyncSession, text: str, status: bool) -> Todo:
    """
    Обновляет задачу по ее id

    Args:
        id (int): id задачи
        text (str): текст задачи
        status (bool): статус задачи

    Returns:
        Todo: обновленная задача
    """

    try:
        todo = await db.get(Todo, id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.text = text
    todo.status = status
    await db.commit()
    await db.refresh(todo)
    return todo
    
    
async def delete_todo(id: int, db: AsyncSession) -> None:
    """
    Удаляет задачу по ее id

    Args:
        id (int): id задачи

    Returns:
        None
    """
    try:
        todo = await db.get(Todo, id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await db.delete(todo)
    await db.commit()
    return
        
