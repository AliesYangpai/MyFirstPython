# 将之前的提示词技巧在这里全都应用上
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_completions(prompt: str, system_prompt: str = "", prefill=""):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
        base_url=os.getenv("OPENAI_API_URL_OLLAMA"),
    )
    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill},
        ],
        temperature=0.0
    )
    ret = response.choices[0].message.content
    print(f"response:{ret} \n token:{response.usage}")


ROLE = "你是一个专业的足球解说员，你从业20多年，工作经验丰富，场控能力应变能力极强，你本人也是足球爱好者。具有丰富的足球专业知识。"
BACKGROUND = "这是2026年世界杯，你在中国进行转播解说。"
THINKING = "你回答问题时，总会分析，拆解问题，并按照步骤一步步思考，思考依照的是论点，论证，论据的科学方式展开，确实不知道的事物，则回答不知道。"
EXAMPLE = ("这里有一个问答的例子，按照这个例子进行回答："
           "用户：你好呀，你是谁呀？"
           "助手：我是一个专业的足球解说员，带你彻底摘除伪球迷标签。")


def generate_prompts():
    prompts = ""
    if ROLE:
        prompts += f"""{ROLE}"""
    if BACKGROUND:
        prompts += f"""\n\n{BACKGROUND}"""
    if THINKING:
        prompts += f"""\n\n{THINKING}"""
    if EXAMPLE:
        prompts += f"""\n\n{EXAMPLE}"""
    return prompts


prompts = generate_prompts()
prefill = "今年西班牙会不会夺冠"
get_completions(prompts, prefill=prefill)
