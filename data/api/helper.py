import aiohttp

from enum import Enum

from data.api.base_api import YOUGILE_API_KEY

class AllowedMethods(str, Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    
session: aiohttp.ClientSession = None

async def init_session():
    global session
    session = aiohttp.ClientSession().__aenter__()
    return session

async def reuse_session():
    global session
    if not session:
        await init_session()
    return session

async def async_request(uri: str, method: str, headers: dict = None, json: dict = None, **kwargs):
    session = reuse_session()

    result = None
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {YOUGILE_API_KEY}"
    }

    async with session.request(method, uri, headers=headers, json=json, **kwargs) as resp:
        if resp.status <= 299:
            result = await resp.json()
        else:
            result = await resp.text()
        return result, resp.status
