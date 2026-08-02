# AutoGen

AutoGen is Microsoft’s framework for building AI agent applications and multi-agent workflows.

This folder is part of my Generative-AI learning repository and contains:
- fundamentals
- core AutoGen concepts
- code examples
- multi-agent projects
- architecture notes
- diagrams and visual explanations

## Why AutoGen

AutoGen is useful when a single LLM is not enough and the task needs:
- planning
- delegation
- collaboration between agents
- tool usage
- human approval
- termination control
- async or multi-step execution

In the stable AutoGen docs, AgentChat is the recommended starting point for beginners, while `autogen-core` gives more flexibility for advanced event-driven systems. :contentReference[oaicite:2]{index=2}

## What you will learn here

- how AutoGen works
- how agents communicate
- how to use `AssistantAgent`
- how to use `UserProxyAgent`
- how to build `RoundRobinGroupChat`
- how `SelectorGroupChat` works
- how termination conditions work
- how memory and tools fit in
- how to build small real-world projects

## Learning path

1. Install and run a model client
2. Create your first agent
3. Understand messages and responses
4. Learn `AssistantAgent`
5. Learn `UserProxyAgent`
6. Build group chat workflows
7. Study termination conditions
8. Explore memory and tool use
9. Build projects

## Folder structure

```text
AutoGen/
├── README.md
├── assets/
│   ├── diagrams/
│   ├── source/
│   └── screenshots/
├── fundamentals/
├── concepts/
└── projects/