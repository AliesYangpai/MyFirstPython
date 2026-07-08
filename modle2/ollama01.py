import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_completion(prompt: str, system_prompt: str = ""):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
        base_url=os.getenv("OPENAI_API_URL_OLLAMA"),
    )

    prev_prompt_tokens = 0
    prev_completion_tokens = 0
    prev_total_tokens = 0
    for index in range(0, 10):
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_API_MODE_QWEN_2_5_3B"),
            max_tokens=300,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
        )
        ret = response.choices[0].message.content
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens

        delta_prompt_tokens = prompt_tokens - prev_prompt_tokens
        delta_completion_tokens = completion_tokens - prev_completion_tokens
        delta_total_tokens = total_tokens - prev_total_tokens

        prev_prompt_tokens = prompt_tokens
        prev_completion_tokens = completion_tokens
        prev_total_tokens = total_tokens


        print(f"index: {index}, "
              f"prompt_tokens: {prompt_tokens}, completion_tokens: {completion_tokens},total_tokens:{total_tokens},"
              f"delta_prompt_tokens: {delta_prompt_tokens}, delta_completion_tokens: {delta_completion_tokens},delta_total_tokens: {delta_total_tokens} content:{ret}")


prompt = "告诉我大海的颜色"
get_completion(prompt)
