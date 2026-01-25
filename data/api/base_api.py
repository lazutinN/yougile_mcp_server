import os

from typing import TypedDict, Union, Dict, Any

YOUGILE_HOST = os.getenv("YOUGILE_HOST")
YOUGILE_API_KEY = os.getenv("YOUGILE_API_KEY")

class YouGileAPIResponse(TypedDict):
    result: Union[Dict[str, Any], str]
    ok: bool
