# Hello MCP - Learning Notes

## Project Objective

The objective of this project is to understand the fundamentals of the **Model Context Protocol (MCP)** by building a simple MCP server using Python.

Unlike traditional APIs, an MCP server exposes Python functions as **tools** that AI applications can discover and execute automatically.

---

# What is MCP?

The **Model Context Protocol (MCP)** is an open standard that enables AI applications to communicate with external tools, data, and services through a standardized interface.

Instead of creating custom integrations for every AI application, developers expose capabilities through an MCP server.

Any MCP-compatible client can then discover and use those capabilities.

---

# Why was MCP introduced?

Before MCP:

- Every AI application required a separate integration.
- Developers repeatedly implemented the same APIs.
- No standard communication protocol existed.

MCP solves this problem by introducing a common protocol between AI clients and external systems.

---

# What is an MCP Server?

An MCP Server is an application that exposes functionality through the Model Context Protocol.

The server contains:

- Tools
- Resources
- Prompts

Clients discover these capabilities automatically.

Example:

```
Calculator Server

Tool:
add(a, b)
```

An AI client can invoke this tool without knowing how it is implemented internally.

---

# What is FastMCP?

FastMCP is the Python SDK used to build MCP servers.

It provides decorators and helper methods for registering tools, resources, and prompts.

Example:

```python
mcp = FastMCP("Hello MCP")
```

This creates an MCP server named **Hello MCP**.

---

# What is a Tool?

A Tool is simply a Python function exposed through MCP.

Example:

```python
@mcp.tool()
def greet(name: str):
    return f"Hello {name}"
```

Clients can discover and execute this function.

---

# What is Tool Registration?

When Python executes

```python
@mcp.tool()
```

FastMCP automatically registers the function.

Conceptually:

```
Registered Tools

• greet()
• add()
• get_profile()
```

No manual configuration is required.

---

# What is Tool Discovery?

When an MCP client connects, it asks the server:

> "What tools are available?"

The server returns metadata describing each registered tool.

The client then builds the UI automatically.

---

# Why are Docstrings Important?

Example:

```python
@mcp.tool()
def greet(name: str):
    """Greet a user."""
```

The docstring becomes the tool description inside the MCP client.

Without a docstring, the client has little context about the tool's purpose.

---

# Why are Type Hints Important?

Example:

```python
def add(a: int, b: int):
```

FastMCP converts the type hints into a JSON Schema.

The MCP client uses that schema to generate input fields automatically.

Example:

```
a : [____]

b : [____]
```

No frontend code is required.

---

# What is JSON Serialization?

Python objects returned by a tool are converted into JSON before being sent back to the client.

Example:

```python
return {
    "name": "Kiran",
    "role": "Software Engineer"
}
```

The client receives a JSON object.

---

# Request Lifecycle

```
User

   │

   ▼

MCP Client

   │

   ▼

Discovers Tools

   │

   ▼

Invokes Tool

   │

   ▼

Hello MCP Server

   │

   ▼

Python Function

   │

   ▼

JSON Response

   │

   ▼

MCP Client
```

---

# Project Components

## server.py

Contains the MCP server and tool definitions.

## requirements.txt

Contains the project dependencies.

## README.md

Project documentation.

## info.md

Learning notes and interview preparation.

---

# Important Terminology

| Term | Meaning |
|------|---------|
| MCP | Model Context Protocol |
| Server | Exposes tools to clients |
| Client | Discovers and invokes tools |
| Tool | Python function exposed through MCP |
| FastMCP | Python SDK for building MCP servers |
| Inspector | Tool used to test MCP servers |
| JSON Schema | Defines tool input parameters |

---

# Common Errors

### Tool not appearing

Possible causes:

- Missing `@mcp.tool()`
- Server not restarted
- Inspector not reconnected

---

### ModuleNotFoundError

Cause:

```
No module named 'mcp'
```

Solution:

- Activate the virtual environment.
- Install dependencies.

```
pip install -r requirements.txt
```

---

### Wrong Python Interpreter

Cause:

Inspector uses a different Python executable.

Solution:

Configure the Inspector to use the virtual environment's Python interpreter.

---

# Interview Questions

## Basic

- What is MCP?
- Why was MCP created?
- What problem does MCP solve?
- What is an MCP Server?
- What is an MCP Client?
- What is FastMCP?
- What is a Tool?
- What is MCP Inspector?

---

## Intermediate

- How does `@mcp.tool()` work?
- How are tools discovered?
- Why are docstrings important?
- How do type hints help MCP?
- How are Python functions converted into tools?
- What happens when `mcp.run()` is called?

---

## Advanced

- Explain the complete request lifecycle.
- How would you expose an existing Python function as an MCP tool?
- Can an MCP tool return complex objects?
- How would you debug a missing tool?
- What happens if two tools have the same name?

---

# Key Takeaways

- MCP standardises communication between AI applications and external systems.
- FastMCP makes it easy to build MCP servers in Python.
- Python functions become MCP tools using the `@mcp.tool()` decorator.
- Clients automatically discover tools without manual configuration.
- Type hints generate input schemas.
- Docstrings provide tool descriptions.
- Python objects are automatically serialized into JSON responses.
- MCP Inspector is useful for testing and debugging MCP servers.