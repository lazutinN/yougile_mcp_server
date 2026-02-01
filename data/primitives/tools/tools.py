from transport.communication import mcp

from data.api.tasks.get_list import TaskListRequest, tasks_list
from data.api.tasks.update_task import UpdateTaskRequest, update_task
from data.api.tasks.get_task import task_by_id
from data.api.tasks.create_task import TaskRequestBodyPayload, create_task
from data.primitives.tools.helper import inner_request_error

@mcp.tool(
        name="TasksList",
        description="Retrieve a list of available tasks",  
)
async def get_tasks_list(query_params: TaskListRequest = None):
    tasks = await tasks_list(query_params)
    if not tasks["ok"]:
        return inner_request_error(tasks)
    response = (
        f"Number of tasks available: {tasks['result']['paging']['count']}\n"
        f"Tasks: {tasks['result']['content']}"
    )
    return "\n---\n" + response


@mcp.tool(
        name="UpdateTask",
        description="Update task by id",  
)
async def put_update_task(task_id: str, body: UpdateTaskRequest):
    res = await update_task(task_id, body)
    if not res["ok"]:
        return inner_request_error(res)
    response = f"Task was successfully update: {res["ok"]}"
    return "\n---\n" + response


@mcp.tool(
        name="GetTask",
        description="Get task by id",
)
async def get_task_by_id(task_id: str):
    task = await task_by_id(task_id)
    if not task["ok"]:
        return inner_request_error(task)
    response = f"Task-id {task_id} details:\n{task['result']}"
    return "\n---\n" + response


@mcp.tool(
        name="CreateTask",
        description="Create a new task",
)
async def get_task_by_id(body: TaskRequestBodyPayload):
    task = await create_task(body)
    if not task["ok"]:
        return inner_request_error(task)
    response = f"Task was successfully created:\n{task['result']}"
    return "\n---\n" + response
