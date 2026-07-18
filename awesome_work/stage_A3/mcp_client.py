import asyncio

# -1- 导入库
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# -2- 实例化客户端和传输
server_parameters = StdioServerParameters(
    command="mcp",  # 执行的关键命令
    args=["run", "mcp_server.py"]  # 执行的关键命令和server文件
)



# -2- 实例化客户端和传输（这里实际上就是开始session会话并执行本次调用任务了）
async def run_init_connect(server_parameters: StdioServerParameters) -> None:
    async with stdio_client(server_parameters) as (read, write):  # 初始化客户端对象
        async with ClientSession(read, write) as session:  # 创建session
            ret = await session.initialize()  # 初始化链接
            print(f"run_init_connect ret:{ret.serverInfo.name}")
            await show_tools_and_resource(session) # 展示工具
            await do_call_tool(session)
            await do_call_resource("goodmorning",session)



# -3- 列出服务器功能
async def show_tools_and_resource(session: ClientSession) -> None:
    tools = await session.list_tools()
    for tool in tools.tools:
        print(f"show_tools_and_resource tool_name:{tool.name}")
    resources = await session.list_resources()
    for resource in resources.resources:
        print(f"show_resources resource_name:{resource.name}")


async def do_call_tool(session: ClientSession) -> None:
    result = await session.call_tool("add", arguments={"a": 12, "b": 18})
    print(f"do_call_tool result:{result.content[0].text}")


async def do_call_resource(tip: str, session: ClientSession) -> None:
    result = await session.read_resource(f"greeting://{tip}")
    print(f"do_call_resource tip:{tip} result:{result.contents}")


if __name__ == "__main__":
    asyncio.run(run_init_connect(server_parameters))
