from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import TypedDict

from data.api.helper import async_request
from data.api.base_api import YOUGILE_HOST, YouGileAPIResponse
from data.api.helper import AllowedMethods


class DeadlinePayload(TypedDict):
    deadline: int
    startDate: int
    withTime: bool
    history: List[str]
    blockedPoints: List[str]
    links: List[str]


class TimeTrackingPayload(TypedDict):
    plan: float
    work: float


class ChecklistItemPayload(TypedDict):
    title: str
    isCompleted: bool


class ChecklistPayload(TypedDict):
    title: str
    items: List[ChecklistItemPayload]


class StopwatchPayload(TypedDict):
    running: bool


class TimerPayload(TypedDict):
    running: bool
    seconds: float


class DealPayload(TypedDict):
    dealAmount: float
    contactPersonIds: List[str]
    organizationId: str
    customFields: Dict[str, Any]


class TaskRequestBodyPayload(TypedDict):
    title: str
    columnId: str
    description: str
    archived: bool
    completed: bool
    subtasks: List[str]
    assigned: List[str]
    deadline: DeadlinePayload
    timeTracking: TimeTrackingPayload
    checklists: List[ChecklistPayload]
    stickers: Dict[str, str]
    color: str
    idTaskCommon: str
    idTaskProject: str
    stopwatch: StopwatchPayload
    timer: TimerPayload
    deal: DealPayload


async def create_task(task_id: str, body: TaskRequestBodyPayload) -> YouGileAPIResponse:
    uri = f"{YOUGILE_HOST}/tasks/{task_id}"
    method = AllowedMethods.PUT.value
    res, status = await async_request(uri, method=method, json=body)
    response = YouGileAPIResponse(
        result=res,
        ok= True if status <= 299 else False)
    if not response["ok"]:
        response.update({"status": status})

    return response
