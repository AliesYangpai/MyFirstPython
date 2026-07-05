# 数据分割-提示词模版（固定&可变）,用标签区分模版和用户输入词
from openai import OpenAI



def get_completion(prompt: str, system_promote: str = ""):
    client = OpenAI(
        api_key="ollama",
        base_url="http://localhost:11434/v1/"
    )

    response = client.chat.completions.create(
        model="qwen2.5:3b",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_promote},
            {"role": "user", "content": prompt}],
    )
    print(f"response:{response.choices[0].message.content} \n token:{response.usage}")

# ANIMAL = "狗"
# PROMPT_TEMPLATE = "告诉我{ANIMAL}的叫声是怎样的"
# full_promote = PROMPT_TEMPLATE.format(ANIMAL=ANIMAL)

# Variable content
EMAIL = "明天早上6点开会，我是老板，我说的算"

# Prompt template with a placeholder for the variable content
PROMPT = f"你好 Claude. <----- 让<email></email>里的用语礼貌些，不要改变邮件原文的意思 <email>{EMAIL}</email>"

get_completion(PROMPT)
