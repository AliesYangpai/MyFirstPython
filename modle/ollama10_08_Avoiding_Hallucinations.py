# 避免Ai幻觉,提示词备回答前要有依据（论点，论证，论据）,知之为知之不知
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
def get_completions(prompt: str, system_prompt: str = ""):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
        base_url=os.getenv("OPENAI_API_URL_OLLAMA")
    )
    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")


prompt = "Who is the heaviest hippo of all time"
prompt_templet = f"the answer of <prompt>{prompt}</prompt> must be in Chinese to reply if you know, and prove it before delivering"
get_completions(prompt_templet)
