from fastapi import APIRouter

from src.api.short_url import router as short_url_router

main_router = APIRouter()
main_router.include_router(short_url_router)
