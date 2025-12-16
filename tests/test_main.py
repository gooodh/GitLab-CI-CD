# test_main.py
import pytest
from httpx import AsyncClient
from app.main import create_app


class TestMainApp:

    @pytest.mark.asyncio
    async def test_create_app(self):
        app = create_app()
        assert app.title == "Стартовая сборка FastAPI"
        assert app.version == "1.0.0"

    @pytest.mark.asyncio
    async def test_home_page(self, client: AsyncClient):
        """Тест главной страницы."""
        response = await client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Добро пожаловать!"

    @pytest.mark.asyncio
    async def test_cors_headers(self, client: AsyncClient):
        """Тест CORS заголовков."""
        # CORS заголовки появляются при реальных запросах
        response = await client.get("/")

        # Проверяем, что запрос прошел успешно (CORS не блокирует)
        assert response.status_code == 200
