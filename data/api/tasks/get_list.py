from typing import TypedDict
from urllib.parse import urlencode

from data.api.helper import async_request
from data.api.base_api import YOUGILE_HOST, YouGileAPIResponse
from data.api.helper import AllowedMethods

class TaskListRequest(TypedDict, total=False):
    assignedTo: str
    columnId: str
    includeDeleted: bool
    limit: int
    offset: int
    stickerId: str
    stickerStateId: str
    title: str


async def tasks_list(query_params: TaskListRequest = None) -> YouGileAPIResponse:
    uri = f"{YOUGILE_HOST}/task-list"

    method = AllowedMethods.GET.value
    
    if query_params:
        uri = f"{uri}?{urlencode(query_params)}"
        
    resp, status = await async_request(uri, method=method)
    response = YouGileAPIResponse(
        result = resp,
        ok = True if status < 300 else False)
    if not response["ok"]:
        response.update({"status": status})

    return response
