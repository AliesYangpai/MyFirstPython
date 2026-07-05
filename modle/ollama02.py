# ollama本地模型100次请求，查看中英token消耗情况
# 依赖：ollama环境安装，model：qwen2.5:3b
from openai import OpenAI
import os

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1/"
)

PROMPTS = {
    "中文": "用一句话描述一只猫在做什么。",
    "English": "Describe in one sentence what a cat is doing.",
}


for i in range(0, 100):
    prompt_ch = PROMPTS["中文"]
    prompt_en = PROMPTS["English"]

    for key, value in PROMPTS.items():
        response = client.chat.completions.create(
            model="qwen2.5:3b",
            max_tokens=100,
            messages=[{"role": "user", "content": value}],
        )
        print(f"{key} prompt_token: {response.usage.prompt_tokens}, complete_tokens:{response.usage.completion_tokens},total_tokens:{response.usage.total_tokens}")

# 基于ollama， model="qwen2.5:3b" 的100问答结果统计
# 指标	                    中文	    英文	    差异（英文 - 中文）
# 平均 Prompt Tokens	        37.0	39.0	+2.0
# 平均 Completion Tokens	    12.9	17.3	+4.4
# 平均 Total Tokens	        49.9	56.3	+6.4
# Prompt Tokens 标准差	      0	      0	    固定值，无波动
# Completion Tokens 波动范围	9 ~ 24	11 ~ 28	英文波动范围更大

