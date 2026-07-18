from mcp.server import FastMCP
# 1.创建一个MCP服务器
mcp = FastMCP("Demo")

# 2.添加一个add的加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    ret = a + b
    print(f"add ret:{ret}")
    return ret

@mcp.tool()
def sub(a: int, b: int) -> int:
    ret= a - b
    print(f"sub ret:{ret}")
    return ret

# 3.添加一个动态问候的资源
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    print(f"get greeting:{name}")
    return f"hello {name}"

# 4.执行服务器运行
if __name__ == "__main__":
    mcp.run()
