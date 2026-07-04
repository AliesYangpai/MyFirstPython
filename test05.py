import json
from urllib import request

def fetch_torvalds():
    url = "https://api.github.com/users/torvalds"
    try:
        req = request.Request(url, headers={"User-Agent": "MyFirstPython/1.0"})
        with request.urlopen(req,timeout=10) as res:
            data = json.loads(res.read().decode("utf-8"))
            print(f"followers are {data['followers']}")

    except Exception as e:
        print(f"请求失败：{e}")


fetch_torvalds()
