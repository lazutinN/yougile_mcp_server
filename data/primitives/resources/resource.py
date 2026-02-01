import json
import os
import pathlib
import aiohttp

from transport.communication import mcp

ROOT_PWD = pathlib.Path("data/primitives/resources")
FILE_NAME = "openapi-spec.json"
SPEC_PWD = ROOT_PWD / FILE_NAME
OPENAPI_SPEC_URL = "https://ru.yougile.com/api-json"

client_session = None

async def _raise_session():
    client_session = await aiohttp.ClientSession().__aenter__()
    return client_session

async def reuse_session():
    global client_session
    if not client_session:
        client_session = await _raise_session()
    return client_session

async def async_request(uri: str, method: str, **kwargs):
    session = await reuse_session()
    async with session.request(method, uri, **kwargs) as res:
        try:
            result = await res.json()
        except:
            result = await res.text()
    return result

@mcp.resource(uri=f"resource://{SPEC_PWD}")
async def openapi_spec():
    spec_pwd = os.path.abspath(SPEC_PWD)

    with open(spec_pwd, 'rb') as file:
        content = file.read()
        spec = json.loads(content)
        file.close()
    return spec
