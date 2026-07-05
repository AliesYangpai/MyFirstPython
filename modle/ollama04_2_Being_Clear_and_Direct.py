# 让回答言简意赅，按照你的意思回答（给提示词丰富的上下文）
from openai import OpenAI

def get_completion(promote: str, system_promote=""):
    client = OpenAI(
        api_key="ollama",
        base_url="http://localhost:11434/v1/"
    )

    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_promote},
            {"role": "user", "content": promote}],
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")


promote = "Who is the best basketball player of all time?Yes, there are differing opinions, but if you absolutely had to pick one player, who would it be"
get_completion(promote,"")
