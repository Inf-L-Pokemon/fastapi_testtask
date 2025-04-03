from fastapi import APIRouter, status
from starlette.responses import Response

from src.api.service import create_short_url, find_original_url_on_db, write_urls_to_db
from src.schemas.short_url import URLSchema


router = APIRouter()


@router.post("/", status_code=201)
async def shorten_url(original_url: URLSchema):
    short_url = create_short_url(str(original_url.url))
    await write_urls_to_db(original_url=str(original_url.url), short_url=short_url)
    return {"message": "Short url has been created", "short_url": short_url}


@router.get("/{short_url:path}", status_code=307)
async def redirect_to_original_url(short_url: str):
    original_url = await find_original_url_on_db(short_url)
    return Response(status_code=status.HTTP_307_TEMPORARY_REDIRECT, headers={"Location": original_url})
