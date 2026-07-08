import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_flower_count(url: str) -> str:
    github_token = os.environ.get("GITHUB_TOKEN", "")
    response = requests.get(url, headers={"User-Agent": "MyFirstPython/1.0",
                                          "Authorization": f"Bearer {github_token}"
                                          })
    code = response.status_code
    print(code)
    data = None
    if code == 200:
        data = response.json().get('followers')
    return data


url = "https://api.github.com/users/torvalds"
flower = get_flower_count(url)
print(f"flower are {flower}")
