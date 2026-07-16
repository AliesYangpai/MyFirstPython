from awesome_work.stage_01.ai_work.ai_work_async import AiWorkAsync
from awesome_work.stage_01.ai_work.ai_work_mgr import AiWorkMgr
from awesome_work.stage_01.ai_work.ai_work_sync import AiWorkSync


class BizWorkMgr:
    def __init__(self):

        # __ai_work = AiWorkSync()
        __ai_work = AiWorkAsync()
        self.__ai_work_mgr: AiWorkMgr = AiWorkMgr(__ai_work)

    def do_chat(self, user_prompt: str) -> None:
        self.__ai_work_mgr.create_msg(user_prompt)

    def do_translate(self, my_tip_info: tuple) -> None:
        tip, type = my_tip_info
        user_prompt = f"将{tip}按照{type}翻译，只给我输翻译结果即可。"
        ret_content = self.__ai_work_mgr.create_msg(user_prompt)
        print(f"do_translate ret_content:{ret_content}")

    def do_loop_chatting(self) -> None:
        chatting_list = []
        while True:
            user_input = input("user:")
            if user_input.lower() == "quit":
                break
            chatting_list.append({"role": "user", "content": user_input})
            ret_assistant_content = self.__ai_work_mgr.create_msg_messages(chatting_list)
            print(f"do_loop_chatting ret_assistant_content:{ret_assistant_content}")
            chatting_list.append({"role": "assistant", "content": ret_assistant_content})

    def do_stream_response(self, user_prompt: str) -> None:
        self.__ai_work_mgr.create_msg_stream(user_prompt)
