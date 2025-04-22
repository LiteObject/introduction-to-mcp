"""
A simple MCP server example using FastMCP.

This script demonstrates how to create a minimal MCP server with a single calculator tool.
It loads environment variables from a .env file, sets up the server, and exposes an 'add' tool
that adds two integers together. The server can run using either stdio or SSE transport.

Dependencies:
    - mcp-server
    - python-dotenv

Usage:
    python server.py

Environment:
    Expects a .env file in the parent directory for configuration.
"""

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,  # only used for SSE transport (set this to any port)
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of a and b.
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """ 
    Subtracts the second integer from the first and returns the result.

    Args: 
        a (int): The number to subtract from. 
        b (int): The number to subtract.

    Returns: 
        int: The result of a - b. 
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """ 
    Multiplies two integers and returns the product.

    Args: 
        a (int): The first integer. 
        b (int): The second integer.

    Returns: 
        int: The product of a and b. 
    """
    return a * b

# Run the server
if __name__ == "__main__":
    TRANSPORT = "sse"
    if TRANSPORT == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif TRANSPORT == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {TRANSPORT}")
