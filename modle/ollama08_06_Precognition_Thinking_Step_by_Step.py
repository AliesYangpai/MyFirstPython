#用系统提示词和step by step来引导模型，先思考，再作答
from openai import OpenAI


def get_completions(prompt: str, system_prompt: str = ""):
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
        ]
    )

    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")
# system_prompt = "你是一个专业的影评电影人"
# prompt = ("这部电影到底是好还是不好呢？"
#           "先将分析思路写入到 xml的tag中，之后再回答。这部电影无论是从创新，还是从情节上都令我非常震撼，不过我在1900年以后就已经是一个置身事外的老古董了")


system_prompt = "你是一个专业的影评电影人"
prompt = "给我输出一个著名的电影名称，并且其主角是出生在1956年的。你先头脑风暴下出生于1956年的电影人，并将结果放进tag中，之后再给出答案"
get_completions(prompt,system_prompt)