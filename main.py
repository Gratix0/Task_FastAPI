from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Таблицы удалены")
    await create_tables()
    print("Таблицы созданы")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)


class Task(BaseModel):
    name: str
    desc: Optional[str] = None


