from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hello who are you ? "}],
)
print(response.choices[0].message.content)
#本章要点：
# 不同的apikey 使用的平台api也是不一样的，deepseek和anthropic 就完全不同
