# promote角色定义，角色背景定义 role-system.
from openai import OpenAI


def get_completion(promote: str, system_promote=""):
    client = OpenAI(
        api_key="ollama",
        base_url="http://localhost:11434/v1/"
    )

    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_promote},
            {"role": "user", "content": promote}],
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")


promote = "你觉的滑雪怎么样？"
get_completion(promote, "你是一只猫")
