from data.api.helper import async_request
from data.api.base_api import YOUGILE_HOST, YouGileAPIResponse
from data.api.helper import AllowedMethods
from data.api.tasks.create_task import TaskRequestBodyPayload

class UpdateTaskRequest(TaskRequestBodyPayload):
    deleted: bool

async def update_task(task_id: str, body: UpdateTaskRequest) -> YouGileAPIResponse:
    uri = f"{YOUGILE_HOST}/tasks/{task_id}"
    method = AllowedMethods.PUT.value
    res, status = await async_request(uri, method=method, json=body)
    response = YouGileAPIResponse(
        result=res,
        ok= True if status <= 299 else False)
    if not response["ok"]:
        response.update({"status": status})

    return response
