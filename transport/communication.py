import data.primitives.tools.tools

from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

def run() -> None:
    mcp.run(transport="streamable-http", json_response=True)
