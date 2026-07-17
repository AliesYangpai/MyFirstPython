import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from awesome_work.stage_01.ai_work.ai_work import AiWork


class AiWorkAsync(AiWork):

    def __init__(self):
        super().__init__()
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
            base_url=os.getenv("OPENAI_API_URL_OLLAMA"),
        )

    def _init_mode(self) -> None:
        load_dotenv()

    def _create_msg(self, user_prompt: str) -> str | None:
        return asyncio.run(self.__create_msg(user_prompt))

    def _create_msg_roles_test(self, user_prompt: str) -> str | None:
        return asyncio.run(self.__create_msg_roles_test(user_prompt))

    def _create_msg_messages(self, message_list: list[dict]) -> str | None:
        return asyncio.run(self.__create_msg_messages(message_list))

    def _create_msg_stream(self, user_prompt: str) -> None:
        asyncio.run(self.__create_msg_stream(user_prompt))

    def _create_msg_system_prompt(self, user_prompt: str, system_prompt: str) -> str | None:
        return asyncio.run(self.__create_msg_system_prompt(user_prompt, system_prompt))

    async def __create_msg(self, user_prompt: str) -> str | None:
        response = await self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=300,
            temperature=0.1
        )
        ret_content = response.choices[0].message.content
        ret_usage = response.usage
        print(f"__create_msg ret_usage: {ret_usage} ret_content: {ret_content}")
        return ret_content

    async def __create_msg_roles_test(self, user_prompt: str) -> str | None:
        response = await self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt},
                      {"role": "assistant", "content": "给你来个巴斯光年的故事吧"},
                      {"role": "user", "content": "好的，就选它了，飞向宇宙浩瀚无垠"}
                      ],
            max_tokens=300,
            temperature=0.1
        )
        ret_content = response.choices[0].message.content
        ret_usage = response.usage
        print(f"__create_msg_roles_test ret_usage: {ret_usage} ret_content: {ret_content}")
        return ret_content

    async def __create_msg_messages(self, message_list: list[dict]) -> str | None:
        response = await self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=message_list,
            max_tokens=300,
            temperature=0.1
        )
        ret_content = response.choices[0].message.content
        return ret_content

    async def __create_msg_stream(self, user_prompt: str) -> None:
        response = await self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=300,
            temperature=0.1,
            stream=True
        )
        async for chunk in response:
            delta = chunk.choices[0].delta
            if delta is not None:
                print(delta.content, end="", flush=True)

    async def __create_msg_system_prompt(self, user_prompt: str, system_prompt: str) -> str | None:
        response = await self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt},
                      {"role": "system", "content": system_prompt},],
            max_tokens=300,
            temperature=0.1,
        )
        ret_content = response.choices[0].message.content
        print(f"_create_msg_system_prompt ret_content: {ret_content}")
        if ret_content:
            return ret_content
        return None
