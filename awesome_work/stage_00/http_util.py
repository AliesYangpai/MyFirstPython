import asyncio

import aiofiles
import aiohttp
import requests
import yaml

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

    async def execute_open_file(self, file_path: str) -> None:
        try:
            async with aiofiles.open(file_path, 'r', encoding="utf-8") as f:
                lines = await f.readlines()
                for line in lines:
                    print(line.strip())
        except Exception as e:
            print(f"execute_open_file error:{e}")

    def open_file(self, file_path: str) -> None:
        asyncio.run(self.execute_open_file(file_path))

    async def execute_write_file(self, file_path, msg) -> None:
        try:
            async with aiofiles.open(file_path, 'w', encoding="utf-8") as f:
                for index in range(0, 9):
                    await f.write(msg + "\n")
        except Exception as e:
            print(f"execute_write_file error:{e}")

    def write_file(self, file_path: str, msg: str) -> None:
        asyncio.run(self.execute_write_file(file_path, msg))

    async def execute_write_amend_file(self, file_path: str, msg: str) -> None:
        try:
            async with aiofiles.open(file_path, 'a', encoding="utf-8") as f:
                for index in range(0, 4):
                    await f.write(msg + "\n")
        except Exception as e:
            print(f"execute_write_amend_file error:{e}")

    def write_amend_file(self, file_path: str, msg: str) -> None:
        asyncio.run(self.execute_write_amend_file(file_path, msg))

    async def execute_read_yaml_file(self, file_path: str) -> dict:
        try:
            async with aiofiles.open(file_path, 'r', encoding="utf-8") as f:
                data = await f.read()
                return yaml.safe_load(data)
        except Exception as e:
            print(f"execute_read_yaml_file error:{e}")
            return None

    def read_yaml_file(self, file_path: str) -> dict:
        return asyncio.run(self.execute_read_yaml_file(file_path))

    async def execute_write_yaml_file(self, file_path: str, dict: dict) -> None:
        try:
            async with aiofiles.open(file_path, 'r', encoding="utf-8") as f:
                str_data = await f.read()
                config_data = yaml.safe_load(str_data)
            config_data |= dict
            async with aiofiles.open(file_path, 'w', encoding="utf-8") as f:
                await f.write(yaml.dump(config_data, allow_unicode=True, sort_keys=False, default_flow_style=False))

        except Exception as e:
            print(f"execute_write_yaml_file error:{e}")

    def write_yaml_file(self, file_path: str, dict: dict) -> None:
        asyncio.run(self.execute_write_yaml_file(file_path, dict))

    async def execute_fetch_async2(self, url: str, token: str = "") -> None:
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"token {token}"  # 标准鉴权格式
                }
                response = await session.request(url=url, method="GET", headers=headers)
                if response.status == 200:
                    print(f"execute_fetch_async2 code:{response.status}")
                else:
                    print(f"execute_fetch_async2 code:{response.status}")
        except Exception as e:
            print(f"execute_fetch_async2 error:{e}")

    def fetch_async2(self, url: str, token: str = "") -> None:
        asyncio.run(self.execute_fetch_async2(url, token))