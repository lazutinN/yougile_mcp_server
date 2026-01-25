import logging

from typing import List, Any, TypedDict, Dict
from urllib.parse import urlencode
from pydantic import TypeAdapter, ValidationError

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

class PagingObject(TypedDict, total=False):
    limit: int
    offset: int
    next: bool
    count: int

class TasksListResponse(TypedDict):
    paging: PagingObject
    content: List[Dict[str, Any]]

TASKS_LIST_RESPONSE_MODEL = TypeAdapter(TasksListResponse)


async def tasks_list(query_params: TaskListRequest = None) -> YouGileAPIResponse:
    uri = f"{YOUGILE_HOST}/api-v2/task-list"

    method = AllowedMethods.GET.value
    
    if query_params:
        uri = f"{uri}?{urlencode(query_params)}"
        
    resp, status = await async_request(uri, method=method)
    ok = True if status < 300 else False

    if ok:
        try:
            resp = TASKS_LIST_RESPONSE_MODEL.validate_python(resp, extra="ignore")
        except ValidationError:
            logging.exception()
            resp = {"error": "Returned object is inconsistent and mismatches with expected one"}
            ok = False

    return {"result": resp,
            "ok": ok}
