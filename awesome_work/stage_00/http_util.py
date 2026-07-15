import asyncio
from xxlimited_35 import Null

import aiohttp
import requests

from awesome_work.stage_00.entity import HttpResponse


class HttpUtil:
    def __init__(self):
        pass

    def fetch_sync(self, url: str) -> HttpResponse:
        try:
            response = requests.get(url)
            code = response.status_code
            if code == 200:
                http_response = HttpResponse(success=True, data=response.json())
            else:
                http_response = HttpResponse(success=False, data=None, msg=str(code))
            return http_response
        except Exception as e:
            print(f"fetch_sync error:{e}")
            return HttpResponse(success=False, data=None, msg=str(e))

    async def execute_fetch_async(self, url: str) -> HttpResponse:
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.request(url=url, method="GET")
                if response.status == 200:
                    json_response = await response.json()
                    http_response = HttpResponse(success=True, data=json_response)
                else:
                    http_response = HttpResponse(success=False, data=None, msg=str(response.status))
                return http_response
        except Exception as e:
            print(f"fetch_async error:{e}")
            return HttpResponse(success=False, data=None, msg=str(e))

    def fetch_async(self, url: str) -> HttpResponse:
        return asyncio.run(self.execute_fetch_async(url))
