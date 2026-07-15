# 网络请求
# asyncio 异步框架
# aiohttp 异步网络请求
# asyncpg 异步数据库框架

import asyncio

import aiohttp
import requests


def start_connect():
    url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
    response = requests.get(url)
    code = response.status_code
    match code:
        case 200:
            json_data = response.json()
            print(f"title: {json_data['title']} kids: {json_data['kids']} ")
            pass
        case _:
            print(f"code: {code} ")


async def task1() -> int:
    print("async task1 开始执行")
    await asyncio.sleep(5)
    print("async task1 执行完毕")
    return 1


async def task2() -> int:
    print("async task2 开始执行")
    await asyncio.sleep(5)
    print("async task2 执行完毕")
    return 2


async def task_all():
    t1, t2 = await asyncio.gather(task1(), task2())
    print(f"task_all t1:{t1} t2:{t2}")


async def start_async_http():
    async with aiohttp.ClientSession() as session:
        url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
        response = await session.request(method="GET", url=url)
        if response.status != 200:
            print(f"start_async_http error code:{response.status} ")
        else:
            ret_json = await response.json()
            print(f"start_async_http success title:{ret_json['title']} ")


if __name__ == "__main__":
    # start_connect()
    asyncio.run(start_async_http())
