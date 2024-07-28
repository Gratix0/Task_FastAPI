from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import *

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("/add")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)

    return {"ok": True, "task_id": task_id}

@router.get("/get_all")
async def get_tasks() -> list[STask]:
    all_task = await TaskRepository.find_all()
    return {"data": all_task}