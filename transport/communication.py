import asyncio
import json

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("YouGile MCP Server",json_response=True)

async def inject_primitives():
    import data.primitives.tools.tools
    import data.primitives.resources.resource as resource

    if not resource.SPEC_PWD.exists():
        spec = await resource.async_request(resource.OPENAPI_SPEC_URL, "get")
        with open(resource.SPEC_PWD, 'wb') as file:
            file.write(json.dumps(spec).encode())
            file.close()

def run() -> None:
    asyncio.run(inject_primitives())
    mcp.run(transport="streamable-http")
