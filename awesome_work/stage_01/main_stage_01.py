from awesome_work.stage_01.ai_work_mgr import AiWorkMgr
from awesome_work.stage_01.biz_work_mgr import BizWorkMgr

ai_work_mgr = AiWorkMgr()
biz_work_mgr = BizWorkMgr()
if __name__ == "__main__":

    # ai_work_mgr.create_msg01("给我来首唐诗")   #写唐诗
    # biz_work_mgr.do_translate(("兔子","法语")) #开始翻译
    # biz_work_mgr.do_loop_chatting() # 循环对话开始
    biz_work_mgr.do_stream_response("给我来首唐诗")