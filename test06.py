import yaml
# 1. 【写入】先创建一个 yaml 文件（练习用）
config = {
    "name": "awesome-agent",
    "version": 1.0,
    "github_api": "https://api.github.com",
    "timeout": 10
}

def create(path):
    with open(path,"w",encoding="utf-8") as f:
        yaml.dump(config,f, allow_unicode=True)

def read(path):
    with open(path,"r",encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        print(f"==read,yaml_data {yaml_data}")
        return yaml_data

def update(path,key,value):
    yaml_data = read(path)
    yaml_data[key] = value
    with open(path,"w",encoding="utf-8") as f:
        yaml.dump(yaml_data,f,allow_unicode=True)

create("./config.yaml")
read("./config.yaml")
update("./config.yaml","timeout",15)
read("./config.yaml")
