import json
from urllib import request
import asyncio
import aiohttp
from openai import timeout


# def fetch_torvalds():
#     url = "https://api.github.com/users/torvalds"
#     try:
#         req = request.Request(url, headers={"User-Agent": "MyFirstPython/1.0"})
#         with request.urlopen(req,timeout=10) as res:
#             data = json.loads(res.read().decode("utf-8"))
#             print(f"followers are {data['followers']}")
#
#     except Exception as e:
#         print(f"请求失败：{e}")
#
#
# fetch_torvalds()

# 异步方法
# async def fetch_torvalds():
#     url = "https://api.github.com/users/torvalds"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, timeout=10) as response:
#             data = await response.json()
#             print(f"flower:{data['followers']}")
#
#     # async with aiohttp.ClientSession().get(url, timeout=10) as response:
#     # data = await response.json()
#
#
# async def main():
#     await fetch_torvalds()
#
# asyncio.run(main())

async def fetch_torvalds():
    url = "https://api.github.com/users/torvalds"
    async with aiohttp.ClientSession() as session:
      async with session.get(url,timeout = 10) as resp:
          data = await resp.json()
          print(f"flower : {data['followers']}")

async def main():
    await fetch_torvalds()
asyncio.run(main())