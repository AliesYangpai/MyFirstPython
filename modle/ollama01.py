# ollama本地模型一单次请求。
# 依赖：ollama环境安装，model：qwen2.5:3b
from openai import OpenAI
import os

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1/"
)

response = client.chat.completions.create(
    model="qwen2.5:3b",
    max_tokens=100,
    messages=[{"role": "user","content":"hi who are you ? "}],
)
print(f"response: {response.choices[0].message.content}")
print(f"usage:{response.usage}")