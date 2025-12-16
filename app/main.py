from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, APIRouter
from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[dict, None]:
    logger.info("Инициализация приложения...")
    yield
    logger.info("Завершение работы приложения...")


def create_app() -> FastAPI:
    app = FastAPI(
        title="Стартовая сборка FastAPI",
        version="1.0.0",
        lifespan=lifespan,
    )
    register_routers(app)
    return app


def register_routers(app: FastAPI) -> None:
    root_router = APIRouter()

    @root_router.get("/", tags=["root"])
    def home_page():
        return {"message": "Добро пожаловать!"}

    app.include_router(root_router, tags=["root"])


app = create_app()
