"""
MCP STDIO Client Example

This script demonstrates how to connect to an MCP server using stdio transport.
It launches the server as a subprocess, initializes the connection, lists available tools,
and calls the 'add' tool with example arguments.

Dependencies:
    - mcp

Usage:
    python client.py
"""

import asyncio
# import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# nest_asyncio.apply()  # Needed to run interactive python

async def main():
    """
    Launches the MCP server as a subprocess and connects to it using stdio transport.
    Initializes the client session, lists available tools from the server, and calls the 'add' tool
    with example arguments (a=2, b=3), printing the result.
    """
    # Define server parameters
    server_params = StdioServerParameters(
        command="python",  # The command to run your server
        args=["server.py"],  # Arguments to the command
    )

    # Connect to the server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("\nAvailable tools:")
            for tool in tools_result.tools:
                print(f"  • {tool.name}: {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("add", arguments={"a": 2, "b": 3})
            print(f"\n2 + 3 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
