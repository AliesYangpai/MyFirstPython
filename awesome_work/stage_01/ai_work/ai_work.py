from abc import ABC, abstractmethod


class AiWork(ABC):
    def __init__(self) -> None:
        self._init_mode()

    @abstractmethod
    def _init_mode(self) -> None:
        pass

    @abstractmethod
    def _create_msg(self, user_prompt: str) -> str | None:
        pass

    @abstractmethod
    def _create_msg_roles_test(self, user_prompt: str) -> str | None:
        pass

    @abstractmethod
    def _create_msg_messages(self, message_list: list[dict]) -> str | None:
        pass

    @abstractmethod
    def _create_msg_stream(self, user_prompt: str) -> None:
        pass

    @abstractmethod
    def _create_msg_system_prompt(self, user_prompt: str, system_prompt: str) -> str | None:
        pass
