import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
def get_completions(prompt:str,system_prompt:str = ""):

    client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY_OLLAMA"],
        base_url=os.environ["OPENAI_API_URL_OLLAMA"],
    )

    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":prompt},
        ]
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")

prompts = "告诉我天空的颜色"

prompt_templet = f"<prompt>{prompts}</prompt> 你要用诙谐的语言来描述，并且要先思考，再作答，比如：哦，亲爱的用户，那当然是美丽的蓝色啦。"
get_completions(prompt_templet)