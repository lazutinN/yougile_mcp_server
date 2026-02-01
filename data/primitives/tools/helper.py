from data.api.base_api import YouGileAPIResponse

def inner_request_error(data: YouGileAPIResponse):
    return f"Request failed.\nReason: {data.get("result")}\nStatus:{data.get("status")}"
