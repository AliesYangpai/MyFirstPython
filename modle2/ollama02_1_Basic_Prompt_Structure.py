import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
def get_completions(prompt:str,system_prompt:str = ""):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
        base_url=os.getenv("OPENAI_API_URL_OLLAMA")
    )
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_API_MODE_QWEN_2_5_3B"),
        max_tokens=300,
        messages=[{"role":"system","content":system_prompt},
                  {"role":"user","content":prompt},],
        temperature=0.1,
    )
    reply = response.choices[0].message.content
    usage = response.usage
    print(f"reply:{reply} \nusage:{usage}")

system_prompt = "你是一个风趣的果农，拥有多年的种植经验。"
prompt = "告诉我哈密瓜的甜度"
get_completions(prompt = prompt, system_prompt=system_prompt)