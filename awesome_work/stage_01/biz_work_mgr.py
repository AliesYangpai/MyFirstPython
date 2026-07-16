from awesome_work.stage_01.ai_work_mgr import AiWorkMgr


class BizWorkMgr:
    def __init__(self):
        self.ai_work_mgr: AiWorkMgr = AiWorkMgr()

    def do_translate(self, my_tip_info: tuple) -> None:
        tip, type = my_tip_info
        user_prompt = f"将{tip}按照{type}翻译，只给我输翻译结果即可。"
        ret_content = self.ai_work_mgr.create_msg02(user_prompt)
        print(f"do_translate ret_content:{ret_content}")

    def do_loop_chatting(self) -> None:
        chatting_list = []
        while True:
            user_input = input("user:")
            if user_input.lower() == "quit":
                break
            chatting_list.append({"role":"user","content":user_input})
            ret_assistant_content = self.ai_work_mgr.create_msg03(chatting_list)
            print(f"do_loop_chatting ret_assistant_content:{ret_assistant_content}")
            chatting_list.append({"role":"assistant","content":ret_assistant_content})

    def do_stream_response(self,user_prompt:str) -> None:
        self.ai_work_mgr.create_msg04_stream(user_prompt)