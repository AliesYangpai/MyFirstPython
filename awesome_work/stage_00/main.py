from multipart import file_path

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
    # 同步请求
    start_request()
    # 异步请求
    start_request2()

    # 异步读取文件
    file_path = "./testfile.txt"
    # http_util.open_file(file_path)
    # 异步重写文件内容
    # http_util.write_file(file_path,"好好学习，天天向上")
    # 异步，追加文件内容
    http_util.write_amend_file(file_path,"就那么回事儿了，哎～")
    yaml_file_path = "./../../config.yaml"
    config_file = http_util.read_yaml_file(yaml_file_path)
    print(f"yaml: name:{config_file['name']}")

    http_util.write_yaml_file(yaml_file_path,{"author":"albert","author_code":"001"})

    # config_file["author"] = "albert"
    # config_file["author_code"] = "001"
    # http_util.write_yaml(file_path,config_file)