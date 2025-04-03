import pyshorteners
from sqlalchemy import insert, select

from src.database import async_session_maker
from src.models.short_url import Url


def create_short_url(original_url):
    return pyshorteners.Shortener().tinyurl.short(original_url)


async def write_urls_to_db(original_url, short_url):
    async with async_session_maker() as session:
        query = insert(Url).values(original_url=original_url, short_url=short_url)

        await session.execute(query)
        await session.commit()


async def find_original_url_on_db(short_url):
    async with async_session_maker() as session:
        query = select(Url.original_url).where(Url.short_url == short_url)
        result = await session.execute(query)

        return result.scalar_one_or_none()
