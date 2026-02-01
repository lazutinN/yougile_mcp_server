from data.api.helper import async_request
from data.api.base_api import YOUGILE_HOST, YouGileAPIResponse
from data.api.helper import AllowedMethods


async def task_by_id(task_id: str) -> YouGileAPIResponse:
    uri = f"{YOUGILE_HOST}/tasks/{task_id}"

    method = AllowedMethods.GET.value
        
    resp, status = await async_request(uri, method=method)
    response = YouGileAPIResponse(
        result = resp,
        ok = True if status < 300 else False)
    if not response["ok"]:
        response.update({"status": status})

    return response
