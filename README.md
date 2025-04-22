# Introduction to MCP

A minimal MCP server and client example demonstrating basic calculator operations using both SSE and stdio transports.

## Installation

To install all packages from your `requirements.txt` file using `pip`, you can use the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Running the Server
Make sure you have installed the `mcp` package. You can do this by running the following command in your terminal:

```bash
pip install mcp[cli]
```

Then, you can run the `server.py` script using the following command:

```bash
mcp dev server.py
```

You can also run the script using Python directly:

```bash
python server.py
```

Use `python server.py` for normal execution. Use `mcp dev server.py` for development with hot-reloading and a better developer experience.

### Important Note

>When you run `mcp dev server.py`, you are starting the MCP Inspector and its proxy server, not your FastMCP server directly. The MCP Inspector runs its own proxy (default port 6277) and does not use the port (8050) specified in your `server.py`.

>To run your FastMCP server on port 8050 as defined in server.py, you should execute: `python server.py`

>The mcp dev command is for development and debugging with the MCP Inspector, not for running your server directly on the specified port. If you want to use the Inspector, connect your client to the proxy port (6277). If you want your server to listen on 8050, run it with `python server.py`.

## Running the Client

### STDIO Client
Launches the server as a subprocess and connects to it using the `stdio` transport. This is useful for testing and debugging.

```bash
python client_stdio.py
```

### SSE Client
Connects to the server using the `sse` transport. This is useful for real-time updates and notifications.

```bash
python client_sse.py
```

### Links
- [Quickstart for Server Developers](https://modelcontextprotocol.io/quickstart/server)
- [Quickstart for Client Developers](https://modelcontextprotocol.io/quickstart/client)

