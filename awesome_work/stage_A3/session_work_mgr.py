import asyncio
import json
import os

from dotenv import load_dotenv
from mcp import stdio_client, StdioServerParameters, ClientSession
from openai import AsyncOpenAI



class SessionWorkMgr:
    def __init__(self):
        self.server_parameters = StdioServerParameters(
            command="mcp",
            args=["run", "mcp_server.py"]
        )
        load_dotenv()
        self.client_llm = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY_OLLAMA"),
            base_url=os.getenv("OPENAI_API_URL_OLLAMA"),
        )

    def __convert_to_llm_tool__(self, tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }
        return tool_schema

    def start_session(self):
        # 连接mcp server 获取tools，并转换为json-rpc
        # 实例化语言模型传参，得返回。
        # 使用返回调用client的call方法
        asyncio.run(self.__connect_and_work__())

    async def __connect_and_work__(self):
        async with stdio_client(self.server_parameters) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                await session.initialize()

                # 2.获取tools列表，转化为json-rpc
                tool_wrap = await session.list_tools()
                tool_functions = []
                for tool in tool_wrap.tools:
                    print(f" __connect_and_work__ {tool.name}: {tool.description}")
                    tool_functions.append(self.__convert_to_llm_tool__(tool))

                # 3.启动语言大模型
                while True:
                    user_prompt = input("user: ").strip()

                    if user_prompt == "exit":
                        break

                    response = await self.client_llm.chat.completions.create(
                        model="qwen2.5:3b",
                        messages=[{"role": "user", "content": user_prompt}],
                        max_tokens=300,
                        temperature=0.1,
                        tools=tool_functions
                    )

                    # 4.获取返回的数据，并收集好function
                    response_message = response.choices[0].message
                    functions_to_call = []
                    if response_message.tool_calls:
                        for tool_call in response_message.tool_calls:
                            print("TOOL: ", tool_call)
                            name = tool_call.function.name
                            args = json.loads(tool_call.function.arguments)
                            functions_to_call.append({"name": name, "args": args})

                    # 5.执行mcp client的方法调用
                    for function in functions_to_call:
                        result = await session.call_tool(function["name"],function["args"])
                        print(f" method: {function['name']} result: {result}")
