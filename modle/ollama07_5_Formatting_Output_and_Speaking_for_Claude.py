# 用标签来控制输入和输出格式
from openai import OpenAI


def get_completion(prompt: str, system_prompt: str = ""):
    client = OpenAI(
        api_key="ollama",
        base_url="http://localhost:11434/v1/"
    )
    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")

ANIMAL = "河马"
PROMPT = f"写一个关于{ANIMAL}的小短诗歌，并把结果放在<tag>标签里"
get_completion(prompt=PROMPT)
