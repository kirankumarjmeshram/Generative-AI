# Hello MCP

A beginner-friendly introduction to the **Model Context Protocol (MCP)** using **Python** and **FastMCP**.

This project demonstrates how to build your first MCP server, register Python functions as tools, and interact with them using the **MCP Inspector**.

---

## Overview

The goal of this project is to understand the core concepts of the **Model Context Protocol (MCP)** before integrating external services such as GitHub, databases, or vector stores.

It focuses on creating a simple MCP server that exposes Python functions as tools and explains how MCP clients discover and execute those tools.

---

## Project Structure

```text
01_Hello_MCP/
│
├── server.py
├── README.md
├── info.md
└── requirements.txt
```

---

## Tech Stack

- Python
- Model Context Protocol (MCP)
- FastMCP

---

## Features

This project demonstrates:

- Creating an MCP server
- Registering tools using `@mcp.tool()`
- Tool discovery
- Function parameters
- Type hints
- Docstrings
- JSON responses
- Testing with MCP Inspector

---

## Architecture

```text
              MCP Inspector
                     │
                     ▼
              Hello MCP Server
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   say_hello()   greet()      add()
                     │
                     ▼
              JSON Response
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Create a virtual environment

```bash
python -m venv env
```

### Activate the virtual environment

**Windows**

```bash
env\Scripts\activate
```

**Linux/macOS**

```bash
source env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the MCP server.

```bash
python server.py
```

The server will wait for an MCP client to connect.

---

## Testing with MCP Inspector

Launch the MCP Inspector.

```bash
npx @modelcontextprotocol/inspector
```

Configure the server:

| Setting | Value |
|----------|-------|
| Transport | STDIO |
| Command | Python executable |
| Arguments | `server.py` |

Once connected, the Inspector automatically discovers all registered tools.

---

## Available Tools

| Tool | Description |
|------|-------------|
| `say_hello()` | Returns a welcome message |
| `greet(name)` | Greets the supplied user |
| `add(a, b)` | Returns the sum of two numbers |
| `get_profile()` | Returns sample profile information |

> **Note:** The available tools may vary depending on the examples implemented in `server.py`.

---

## Concepts Covered

This project introduces the following MCP concepts:

- MCP Server
- FastMCP
- Tool Registration
- Tool Discovery
- Function Parameters
- Type Hints
- Docstrings
- JSON Serialization
- STDIO Transport
- MCP Inspector

---

## Request Flow

```text
User
 │
 ▼
MCP Inspector
 │
 ▼
Discover Available Tools
 │
 ▼
Invoke Tool
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
MCP Inspector
```

---

## Learning Outcomes

After completing this project, you will understand:

- How to create an MCP server using FastMCP
- How Python functions become MCP tools
- How MCP clients discover available tools
- How tool parameters are generated from type hints
- How docstrings improve tool descriptions
- How Python return values are serialized into JSON
- How to test and debug an MCP server using MCP Inspector