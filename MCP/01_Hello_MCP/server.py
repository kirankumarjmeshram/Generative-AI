from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hello MCP")


@mcp.tool()
def say_hello():
    """Return a welcome message."""
    return "Hello from MCP!"


@mcp.tool()
def greet(name: str):
    """Greet a user."""
    return f"Hello {name}!"


@mcp.tool()
def add(a: int, b: int):
    """Add two numbers."""
    return a + b


@mcp.tool()
def get_profile():
    """Return profile information."""
    return {
        "name": "Kiran",
        "profession": "Software Engineer",
        "country": "India"
    }


if __name__ == "__main__":
    mcp.run()