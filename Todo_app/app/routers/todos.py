from app.schemas import TodoCreate, TodoRead, TodoUpdate
from fastapi import APIRouter, Depends
from app.database import get_db
from app.crud import create_todo, get_todos, delete_todo, update_todo
from typing import List
from fastapi import HTTPException


router = APIRouter(prefix='/todos', tags=['todos'])


@router.post('/', response_model=TodoRead)
async def create_todo_handler(todo: TodoCreate, db=Depends(get_db)):
    return await create_todo(todo.text, db, todo.status)


@router.get('/', response_model=List[TodoRead])
async def get_todos_handler(db=Depends(get_db)):
    return await get_todos(db)


@router.delete('/{id}', response_model=TodoRead)
async def delete_todo_handler(id: int, db=Depends(get_db)):
    return await delete_todo(id, db)

@router.patch('/{id}', response_model=TodoRead)
async def update_todo_handler(id: int, todo: TodoUpdate, db=Depends(get_db)):
    try:
        todo = await update_todo(id, db, todo.text, todo.status)
    except ValueError:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    
    return todo

