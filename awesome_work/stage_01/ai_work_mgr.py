import asyncio
import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


class AiWorkMgr:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
            base_url=os.getenv("OPENAI_API_URL_OLLAMA"),
        )


    def create_msg01(self, use_prompt: str ):
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            max_tokens=300,
            temperature=0.1,
            messages=[
                {"role": "user", "content": use_prompt},
                {"role": "assistant", "content": "给你来一首李白的诗吧"},
                {"role": "user", "content": "嗯，好，我喜欢李白"},
            ]
        )
        ret_content = response.choices[0].message.content
        ret_usage = response.usage
        print(f"create_msg01 ret_content:{ret_content} \n ret_usage:{ret_usage}")

    def create_msg02(self, use_prompt: str)-> str | None:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            max_tokens=300,
            temperature=0.1,
            messages=[
                {"role": "user", "content": use_prompt},
            ]
        )
        ret_usage = response.usage
        print(f"create_msg02 ret_usage:{ret_usage}")
        return response.choices[0].message.content

    def create_msg03(self, message_list: list[Any])-> str:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            max_tokens=300,
            temperature=0.1,
            messages=message_list
        )
        ret_usage = response.usage
        print(f"create_msg03 ret_usage:{ret_usage}")
        return response.choices[0].message.content