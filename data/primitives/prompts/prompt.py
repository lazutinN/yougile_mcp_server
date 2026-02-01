from transport.communication import mcp
from data.primitives.resources.resource import SPEC_PWD

OPENAPI_SPEC_RESOURCE_URI = f"resource://{SPEC_PWD}"

@mcp.prompt(
    name="BuildToolFromOpenAPISpec",
    description="Prompt for MCP clients to create a new tool using the OpenAPI spec resource."
    )
async def build_tool_from_openapi_spec():
    return (
        "You are creating a new MCP tool from the OpenAPI spec.\n"
        f"- First, invoke the resource: {OPENAPI_SPEC_RESOURCE_URI}\n"
        "- Select the best endpoint for the user request (path + method).\n"
        "- Name the tool clearly (action + object) and write a precise description.\n"
        "- Define inputs from parameters and requestBody; mark required fields.\n"
        "- Validate inputs and map them to the API call (path, query, header, body).\n"
        "- Return a concise, user-friendly response with key fields only.\n"
        "- On error, return a failure message with status and reason.\n"
    )
