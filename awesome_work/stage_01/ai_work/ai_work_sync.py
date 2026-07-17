import os

from dotenv import load_dotenv
from openai import OpenAI

from awesome_work.stage_01.ai_work.ai_work import AiWork


class AiWorkSync(AiWork):
    def __init__(self) -> None:
        super().__init__()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
            base_url=os.getenv("OPENAI_API_URL_OLLAMA"),
        )

    def _init_mode(self) -> None:
        load_dotenv(verbose=True)

    def _create_msg(self, user_prompt: str) -> str | None:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=300,
            temperature=0.1,
        )
        ret_content = response.choices[0].message.content
        ret_usage = response.usage
        print(f"_create_msg ret_usage: {ret_usage} \n ret_content: {ret_content}")
        return ret_content

    def _create_msg_roles_test(self, user_prompt: str) -> str | None:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt},
                      {"role": "assistant", "content": "给你来个巴斯光年的故事吧"},
                      {"role": "user", "content": "好的，就选它了，飞向宇宙浩瀚无垠"}
                      ],
            max_tokens=300,
            temperature=0.1,
        )
        ret_content = response.choices[0].message.content
        ret_usage = response.usage
        print(f"_create_msg_roles_test ret_usage:{ret_usage} \n ret_content: {ret_content}")
        return ret_content

    def _create_msg_messages(self, message_list: list[dict]) -> str | None:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=message_list,
            max_tokens=300,
            temperature=0.1,
        )
        ret_content = response.choices[0].message.content
        ret_usage = response.usage
        print(f"_create_msg_messages ret_usage:{ret_usage} \n ret_content: {ret_content}")
        return ret_content

    def _create_msg_stream(self, user_prompt: str) -> None:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=300,
            temperature=0.1,
            stream=True,
        )
        for event in response:
            ret_content_delta = event.choices[0].delta.content
            if ret_content_delta:
                print(f"_create_msg_stream ret_content_delta: {ret_content_delta}")

    def _create_msg_system_prompt(self, user_prompt: str, system_prompt: str) -> str | None:
        response = self.client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[{"role": "user", "content": user_prompt},
                      {"role": "system", "content": system_prompt},
                      ],
            max_tokens=300,
            temperature=0.1,
        )
        ret_content = response.choices[0].message.content
        print(f"_create_msg_system_prompt ret_content: {ret_content}")
        if ret_content:
            return ret_content
        return None
