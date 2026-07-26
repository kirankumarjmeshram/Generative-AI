# GitHub MCP Server

A GitHub **Model Context Protocol (MCP)** server built with **Python**, **FastMCP**, and **PyGithub**.

This project demonstrates how to integrate the GitHub REST API with MCP by exposing common GitHub operations as MCP tools. These tools can be discovered and executed by any MCP-compatible client such as ChatGPT, Claude Desktop, Cursor, VS Code, or the MCP Inspector.

---

## Overview

This project extends the concepts learned in **Hello_MCP** by connecting an external service—the GitHub REST API.

Using a GitHub Personal Access Token (PAT), the server authenticates with GitHub and exposes repository-related operations as MCP tools.

---

## Features

- Authenticate with GitHub using a Personal Access Token
- List repositories
- Retrieve repository details
- List repository branches
- List open issues
- Retrieve the latest commit
- List pull requests
- Retrieve authenticated user information
- Create GitHub issues

---

## Project Structure

```text
02_GitHub_MCP/
│
├── server.py
├── README.md
├── info.md
├── requirements.txt
└── .env.example
```

---

## Tech Stack

- Python
- Model Context Protocol (MCP)
- FastMCP
- PyGithub
- GitHub REST API
- python-dotenv

---

## Architecture

```text
              MCP Client
(ChatGPT / Claude / Cursor / Inspector)
                     │
                     ▼
             GitHub MCP Server
                     │
                     ▼
                PyGithub
                     │
                     ▼
             GitHub REST API
                     │
                     ▼
            GitHub Repository
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Create a virtual environment.

```bash
python -m venv env
```

Activate the virtual environment.

### Windows

```bash
env\Scripts\activate
```

### Linux / macOS

```bash
source env/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GIT_PERSONAL_ACCESS_TOKEN=your_personal_access_token
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

Configure the server using the following settings:

| Setting | Value |
|----------|-------|
| Transport | STDIO |
| Command | Python executable |
| Arguments | `server.py` |

After connecting, the Inspector automatically discovers all registered GitHub tools.

---

## Available Tools

| Tool | Description |
|------|-------------|
| `list_repositories()` | Returns all repositories owned by the authenticated user |
| `get_repository(repo_name)` | Returns repository details |
| `list_branches(repo_name)` | Lists repository branches |
| `list_issues(repo_name)` | Lists open issues |
| `latest_commit(repo_name)` | Returns the latest commit |
| `list_pull_requests(repo_name)` | Lists open pull requests |
| `get_authenticated_user()` | Returns authenticated user information |
| `create_issue(repo_name, title, body)` | Creates a GitHub issue |

---

## MCP Concepts Demonstrated

This project demonstrates the following MCP concepts:

- MCP Server
- Tool Registration
- Tool Discovery
- Function Parameters
- Type Hints
- JSON Responses
- Authentication
- Environment Variables
- External API Integration
- Error Handling
- STDIO Transport

---

## Request Flow

```text
User
 │
 ▼
MCP Client
 │
 ▼
Discover Available Tools
 │
 ▼
Invoke Tool
 │
 ▼
GitHub MCP Server
 │
 ▼
PyGithub
 │
 ▼
GitHub REST API
 │
 ▼
GitHub Response
 │
 ▼
JSON Response
 │
 ▼
MCP Client
```

---

## Learning Outcomes

After completing this project, you will understand:

- How to integrate an external API with an MCP server
- How to authenticate using a GitHub Personal Access Token
- How to expose GitHub operations as MCP tools
- How MCP clients discover and execute tools
- How to use PyGithub to interact with the GitHub REST API
- How to test MCP servers using the MCP Inspector