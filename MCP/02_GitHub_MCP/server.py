from mcp.server.fastmcp import FastMCP
from github import Github, Auth, GithubException
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

git_token = os.getenv("GIT_PERSONAL_ACCESS_TOKEN")

if not git_token:
    raise ValueError("GIT_PERSONAL_ACCESS_TOKEN is not set")

# GitHub Authentication
auth = Auth.Token(git_token)
github = Github(auth=auth)

# Create MCP Server
mcp = FastMCP("GitHub MCP Server")


@mcp.tool()
def list_repositories():
    """List all GitHub repositories."""
    try:
        user = github.get_user()
        return [repo.name for repo in user.get_repos()]
    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def get_repository(repo_name: str):
    """Get repository information."""
    try:
        repo = github.get_user().get_repo(repo_name)

        return {
            "name": repo.name,
            "description": repo.description,
            "language": repo.language,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "watchers": repo.watchers_count,
            "url": repo.html_url,
        }

    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def list_branches(repo_name: str):
    """List all branches."""
    try:
        repo = github.get_user().get_repo(repo_name)

        return [branch.name for branch in repo.get_branches()]

    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def list_issues(repo_name: str):
    """List open issues."""
    try:
        repo = github.get_user().get_repo(repo_name)

        issues = []

        for issue in repo.get_issues(state="open"):
            issues.append({
                "number": issue.number,
                "title": issue.title,
                "state": issue.state,
            })

        return issues

    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def latest_commit(repo_name: str):
    """Get latest commit."""
    try:
        repo = github.get_user().get_repo(repo_name)

        commit = repo.get_commits()[0]

        return {
            "sha": commit.sha,
            "message": commit.commit.message,
            "author": commit.commit.author.name,
            "date": str(commit.commit.author.date),
        }

    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def list_pull_requests(repo_name: str):
    """List open pull requests."""
    try:
        repo = github.get_user().get_repo(repo_name)

        prs = []

        for pr in repo.get_pulls(state="open"):
            prs.append({
                "number": pr.number,
                "title": pr.title,
                "user": pr.user.login,
            })

        return prs

    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def get_authenticated_user():
    """Get authenticated GitHub user."""
    try:
        user = github.get_user()

        return {
            "username": user.login,
            "name": user.name,
            "followers": user.followers,
            "following": user.following,
            "public_repos": user.public_repos,
        }

    except GithubException as e:
        return {"error": str(e)}


@mcp.tool()
def create_issue(repo_name: str, title: str, body: str):
    """Create a GitHub issue."""
    try:
        repo = github.get_user().get_repo(repo_name)

        issue = repo.create_issue(
            title=title,
            body=body
        )

        return {
            "number": issue.number,
            "title": issue.title,
            "url": issue.html_url,
        }

    except GithubException as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()