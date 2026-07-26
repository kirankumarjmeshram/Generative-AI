<div align="center">

# 🚀 Model Context Protocol (MCP)

### Learning • Building • Experimenting with MCP

A collection of notes, experiments, and practical implementations built using the **Model Context Protocol (MCP)** to understand how AI applications communicate with external tools, APIs, databases, and services.

</div>

---

# 📖 What is Model Context Protocol (MCP)?

The **Model Context Protocol (MCP)** is an open standard that enables AI applications to securely communicate with external tools, databases, APIs, file systems, and other services through a standardized interface.

Instead of creating custom integrations for every AI application, MCP defines a common protocol that allows AI clients to discover and interact with capabilities exposed by MCP servers.

Think of MCP as a universal communication layer between AI models and external systems.

---

# 🏛️ Architecture

```text
                          User
                            │
                            ▼
                    AI Application
        (ChatGPT • Claude • Cursor • VS Code)
                            │
                            ▼
                       MCP Client
                            │
                            ▼
                       MCP Server
                            │
      ┌───────────────┬───────────────┬───────────────┐
      ▼               ▼               ▼               ▼
   GitHub API     File System     Databases     REST APIs
      │               │               │               │
      └───────────────┴───────────────┴───────────────┘
                            │
                            ▼
                      Structured Response
```

---

# 🧩 Core Components

## MCP Server

Hosts tools, resources, and prompts that AI applications can use.

---

## MCP Client

Applications capable of communicating using the Model Context Protocol.

Examples

- ChatGPT
- Claude Desktop
- Cursor
- Visual Studio Code
- MCP Inspector

---

## Tools

Executable functions exposed by an MCP server.

Examples

- Query GitHub
- Read files
- Execute SQL
- Search a vector database
- Create GitHub issues

---

## Resources

Structured, read-only information provided to AI models.

Examples

- README files
- Documentation
- Configuration
- Knowledge bases

---

## Prompts

Reusable prompt templates exposed by an MCP server.

---

## Transport

Defines how clients communicate with servers.

Examples

- STDIO
- HTTP
- SSE

---

# 🔄 Request Lifecycle

```text
User
 │
 ▼
AI Client
 │
 ▼
Discover Server Capabilities
 │
 ▼
Select Tool / Resource / Prompt
 │
 ▼
MCP Server
 │
 ▼
External Service
 │
 ▼
Structured Response
 │
 ▼
AI Client
 │
 ▼
User
```

---

# 📂 Repository Structure

```text
MCP/
│
├── README.md
│
├── 01_Hello_MCP/
├── 02_GitHub_MCP/
├── 03_FileSystem_MCP/
├── 04_SQLite_MCP/
├── 05_Postgres_MCP/
├── 06_VectorDB_MCP/
├── 07_RAG_MCP/
├── 08_Agent_MCP/
│
└── assets/
    ├── images/
    └── diagrams/
```

---

# 🧠 Important Concepts

| Concept | Description |
|----------|-------------|
| MCP | Open protocol connecting AI applications with external systems |
| Server | Exposes capabilities to AI clients |
| Client | Consumes capabilities from an MCP server |
| Tool | Executable function callable by AI |
| Resource | Read-only contextual information |
| Prompt | Reusable prompt template |
| Transport | Communication mechanism between client and server |
| FastMCP | Python framework for building MCP servers |
| Inspector | Official tool for testing MCP servers |
| JSON Schema | Tool input schema generated from Python type hints |
| Authentication | Secure access to external services |
| Context | Information supplied to AI models |
| Capability Discovery | Process where clients discover available tools automatically |

---

# 📚 Learning Topics

## Fundamentals

- MCP Overview
- Architecture
- Client–Server Model
- FastMCP
- Python SDK

---

## Tools

- Basic Tools
- Tool Parameters
- Type Hints
- Error Handling
- Tool Metadata

---

## Resources

- Static Resources
- Dynamic Resources
- Resource Templates

---

## Prompts

- Prompt Templates
- Dynamic Prompts
- Prompt Reuse

---

## Communication

- STDIO
- HTTP
- SSE

---

## Authentication

- API Keys
- Personal Access Tokens
- OAuth

---

## Integrations

- GitHub
- File System
- SQLite
- PostgreSQL
- REST APIs
- Vector Databases
- RAG
- AI Agents

---

# 🛠️ Development Workflow

```text
Design
   │
   ▼
Create MCP Server
   │
   ▼
Expose Tools / Resources / Prompts
   │
   ▼
Test using MCP Inspector
   │
   ▼
Integrate with AI Client
   │
   ▼
Deploy
```

---

# 🌐 MCP Ecosystem

```text
                   AI Applications

      ChatGPT    Claude    Cursor    VS Code
           │         │         │         │
           └─────────┴─────────┴─────────┘
                         │
                         ▼
                Model Context Protocol
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    GitHub API      File System      Databases
        │                │                │
        ▼                ▼                ▼
      External Services & Data Sources
```

---

# 🔗 Useful Resources

## Official

- https://modelcontextprotocol.io
- https://spec.modelcontextprotocol.io
- https://github.com/modelcontextprotocol/python-sdk
- https://github.com/modelcontextprotocol/typescript-sdk

---

## Documentation

- https://docs.github.com/en/rest
- https://docs.github.com/en/graphql
- https://pygithub.readthedocs.io

---

## Development Tools

### MCP Inspector

```bash
npx @modelcontextprotocol/inspector
```

---

### Create Virtual Environment

```bash
python -m venv env
```

---

### Activate Environment (Windows)

```bash
env\Scripts\activate
```

---

### Install MCP SDK

```bash
pip install mcp
```

---

# 📌 Notes

This directory serves as a central workspace for learning the **Model Context Protocol** through practical examples, hands-on projects, and real-world integrations.

Each subdirectory focuses on a specific MCP concept or external integration, making it easy to explore and expand knowledge over time.

This README is intended to evolve as new MCP features, SDK updates, and learning projects are added.

---

<div align="center">

**⭐ Building practical MCP servers one project at a time.**

</div>