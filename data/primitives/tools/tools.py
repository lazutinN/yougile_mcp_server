from transport.communication import mcp

from data.api.tasks.get_list import TaskListRequest, tasks_list

@mcp.tool(
        name="Tasks List",
        description="Retrieve a list of available tasks",  
)
async def get_tasks_list(query_params: TaskListRequest = None):
    tasks = await tasks_list(query_params)
    if not tasks["ok"]:
        return f"Request failed: {tasks.get('result')}"
    response = (
        f"Number of tasks available: {len(tasks['result']['content'])}\n"
        f"Tasks: {tasks['result']['content']}"
    )
    return response
