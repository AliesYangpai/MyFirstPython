from awesome_work.stage_00.http_util import HttpUtil

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
http_util = HttpUtil()


def start_request():
    ret = http_util.fetch_sync(url)
    print(f" start_request status: {ret.success} data: {ret.data} msg: {ret.msg}")

def start_request2():
    ret = http_util.fetch_async(url)
    print(f" start_request2 status: {ret.success} data: {ret.data} msg: {ret.msg}")


if __name__ == "__main__":
    start_request()
    # start_request2()