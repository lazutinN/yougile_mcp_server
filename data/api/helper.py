import aiohttp

from enum import Enum
from typing import Tuple

from aiohttp import ClientTimeout

from data.api.base_api import YOUGILE_API_KEY

class AllowedMethods(str, Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    
session: aiohttp.ClientSession = None
DEFAULT_TIMEOUT = ClientTimeout(5.0)

async def init_session():
    global session
    session = await aiohttp.ClientSession().__aenter__()
    return session

async def reuse_session():
    global session
    if not session:
        await init_session()
    return session

async def async_request(uri: str, method: str, headers: dict = None, json: dict = None, **kwargs) -> Tuple[dict | str, int]:
    session = await reuse_session()

    result = None
    headers_ = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {YOUGILE_API_KEY}"
    }
    if headers:
        headers_.update(headers)

    async with session.request(method, uri, headers=headers_, json=json, timeout=DEFAULT_TIMEOUT, **kwargs) as resp:
        if resp.status <= 299:
            result = await resp.json()
        else:
            result = await resp.text()
        return result, resp.status
