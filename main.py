from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Tryingggggggg")

@mcp.tool()
def add(a, b):
    return a+b


@mcp.tool()
def read_file(path: str) -> str:
    """Read a text file"""
    with open(path, "r") as f:
        return f.read()
    

if __name__ == "__main__":
    print("MCP running...")
    mcp.run()




print("Wohoooooo")



print("Hello")
print("Changes on remote for branch testing")
print("Remote First Extra line - Changed 3x")
print("Remote First Extra line - Changed 2x")
print("LOcal First Extra line - Changed 1x")
print("Second Extra line")
