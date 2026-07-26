# GitHub MCP - Learning Notes

## Project Objective

Learn how to integrate the GitHub REST API with the Model Context Protocol (MCP) by exposing GitHub operations as MCP tools.

---

# What You'll Learn

- GitHub API
- Personal Access Tokens
- Authentication
- MCP Tool Design
- API Integration
- Error Handling
- Environment Variables
- Tool Discovery
- JSON Responses

---

# Project Flow

```
User

    │

    ▼

MCP Client

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

GitHub Servers

    │

    ▼

JSON Response

    │

    ▼

MCP Client
```

---

# What is PyGithub?

PyGithub is a Python wrapper around the GitHub REST API.

Instead of manually sending HTTP requests, PyGithub provides Python classes and methods.

Example:

```python
repo = github.get_repo("owner/repository")
```

instead of

```
GET https://api.github.com/repos/owner/repository
```

---

# Why use Personal Access Tokens?

GitHub requires authentication.

Instead of using a username and password, GitHub recommends using Personal Access Tokens (PAT).

Benefits

- More secure
- Configurable permissions
- Easy to revoke
- Supports automation

---

# Why use .env?

Never hardcode secrets.

Bad

```python
token = "ghp_xxxxxxxxx"
```

Good

```python
token = os.getenv("GIT_PERSONAL_ACCESS_TOKEN")
```

---

# Authentication Flow

```
.env

↓

GitHub Token

↓

PyGithub

↓

GitHub API

↓

Authenticated Requests
```

---

# How Tool Registration Works

```
@mcp.tool()
def list_repositories():
```

FastMCP registers the function.

When the client connects, the tool becomes discoverable.

---

# Tool Discovery

Client connects

↓

Server returns

```
list_repositories()

get_repository()

list_branches()

create_issue()
```

Client automatically builds the UI.

---

# Available Tools

## list_repositories()

Returns all repositories.

---

## get_repository()

Returns repository details.

---

## list_branches()

Lists branches.

---

## list_issues()

Lists open issues.

---

## latest_commit()

Returns latest commit.

---

## list_pull_requests()

Lists pull requests.

---

## get_authenticated_user()

Returns authenticated user details.

---

## create_issue()

Creates a GitHub issue.

---

# GitHub API Objects Used

- Github
- Repository
- Branch
- Commit
- PullRequest
- Issue
- NamedUser

---

# Error Handling

Use

```python
GithubException
```

to handle API errors.

Example

- Invalid repository
- Invalid token
- Rate limit exceeded

---

# Common Errors

## Invalid Token

Cause

Wrong PAT

Solution

Generate a new token.

---

## 401 Unauthorized

Cause

Expired token

Solution

Update the token.

---

## 404 Repository Not Found

Cause

Wrong repository name

Solution

Check repository ownership.

---

## Tool Not Appearing

Possible causes

- Missing `@mcp.tool()`
- Server not restarted
- Inspector cache

---

# Interview Questions

## Basic

- What is the GitHub REST API?
- What is PyGithub?
- Why use a Personal Access Token?
- What is authentication?
- Why use `.env`?

---

## Intermediate

- Why use PyGithub instead of requests?
- How does FastMCP expose GitHub functions?
- Explain tool discovery.
- How does authentication work?
- What is rate limiting?

---

## Advanced

- Explain the complete request lifecycle.
- How would you secure the token?
- How would you paginate repositories?
- How would you implement retry logic?
- How would you handle GitHub API failures?
- Difference between REST API and GraphQL API?

---

# Hands-on Exercises

- Add a tool to create a repository.
- Add a tool to delete an issue.
- List repository collaborators.
- List releases.
- List workflows.
- List repository tags.

---

# Key Takeaways

- Learned how MCP integrates external APIs.
- Understood GitHub authentication.
- Learned secure secret management.
- Built multiple MCP tools.
- Connected AI clients to GitHub.
- Understood API request flow.