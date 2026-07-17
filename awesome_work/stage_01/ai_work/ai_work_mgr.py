from awesome_work.stage_01.ai_work.ai_work import AiWork


class AiWorkMgr:
    def __init__(self, ai_work: AiWork) -> None:
        self.ai_work = ai_work

    def create_msg(self, user_prompt: str) -> str | None:
        return self.ai_work._create_msg(user_prompt)

    def create_msg_roles_test(self, user_prompt: str) -> str | None:
        return self.ai_work._create_msg_roles_test(user_prompt)

    def create_msg_messages(self, message_list: list[dict]) -> str | None:
        return self.ai_work._create_msg_messages(message_list)

    def create_msg_stream(self, user_prompt: str) -> None:
        return self.ai_work._create_msg_stream(user_prompt)

    def create_msg_system_prompt(self, user_prompt: str, system_prompt: str) -> str | None:
        return self.ai_work._create_msg_system_prompt(user_prompt, system_prompt)
