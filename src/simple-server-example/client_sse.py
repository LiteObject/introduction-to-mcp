"""
MCP SSE Client Example

This script connects to an MCP server using SSE (Server-Sent Events) transport.
It lists available tools and calls the 'add' tool with example arguments.

Instructions:
    1. Ensure the server is running and configured for SSE transport on port 8050.
    2. Run this script to connect and interact with the server.

Dependencies:
    - mcp

Usage:
    python py
"""

import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    """
    Connects to the MCP server using SSE transport, initializes the session, lists available tools,
    and calls the 'add' tool with example arguments (a=2, b=3), printing the result.
    """
    # Connect to the server using SSE
    async with sse_client("http://localhost:8050/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("add", arguments={"a": 2, "b": 3})
            print(f"2 + 3 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())