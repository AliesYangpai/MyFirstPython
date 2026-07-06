# 用steam流来输出打印效果
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def generate_prompts(prompt: str, system_prompt: str = ""):
    client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY_OLLAMA"],
        base_url=os.environ["OPENAI_API_URL_OLLAMA"],
    )
    stream = client.chat.completions.create(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},],
        temperature=0.1,
        max_tokens=300,
        stream=True,
    )
    for event in stream:
        content = event.choices[0].delta.content
        if content:
            print(content,end="",flush=True)




    # ret = response.choices[0].message.content
    # print(f"response:{ret} \n token:{response.usage}")


prompt = "告诉我天空的颜色"
generate_prompts(prompt)