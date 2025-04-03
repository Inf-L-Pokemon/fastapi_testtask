#!/usr/bin/env python3
import os
import sys
import asyncio
import asyncpg


async def check_db():
    for _ in range(30):
        try:
            conn = await asyncpg.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME"),
                host="db",
                port=5432
            )
            await conn.close()
            return True
        except Exception:
            await asyncio.sleep(1)
    return False

if __name__ == "__main__":
    sys.exit(0 if asyncio.run(check_db()) else 1)
