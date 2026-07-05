# 提示词的基本结构
from platform import system

from openai import OpenAI


def get_completion(promote):
    client = OpenAI(
        api_key="ollama", base_url="http://localhost:11434/v1/"
    )

    # response = client.chat.completions.create(
    #     model="qwen2.5:3b",
    #     max_tokens=300,
    #     messages=[{"role":"user","content":promote}],
    # )

    # 1.因为没有指定提示词角色，所以在user和assistant之间交替失败了。
    # 但是我发现这里应该做了容错（并不是所有模型都有容错，deepseek4 就会直接一场），如果没有传入role，那么为了用户体验，此处会给出模型介绍，
    # response = client.chat.completions.create(
    #     model="qwen2.5:3b",
    #     max_tokens=300,
    #     messages=[{"content":promote}],
    #     temperature=0.0
    # )

    #
    # response = client.chat.completions.create(
    #     model="qwen2.5:3b",
    #     max_tokens=300,
    #     messages=[{"role":"user","content":promote},
    #               {"role":"user","content":"告诉我玫瑰花的颜色"}],
    #     temperature=0.0
    # )

    # 2.messages-role-system 指定系统提示词，这样可以使得答案有不同的效果。
    # openAI这里是在message-role-system中指定，其他API 可能会有差异
    # response = client.chat.completions.create(
    #     model="qwen2.5:3b",
    #     max_tokens=300,
    #     messages=[
    #         {"role": "system", "content": "你是一个学术教授，回答问题要谨慎"},
    #         {"role": "user", "content": promote}],
    #
    #     temperature=0.0
    # )

    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[{"role": "user", "content": promote}],
        temperature=0.0
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")


# promote = "hi Qwen,how are you?"
promote = "你能告诉我海洋的颜色吗？"
get_completion(promote)
