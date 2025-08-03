# importe suas rota da api aqui

from .routes import text
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(text.router)