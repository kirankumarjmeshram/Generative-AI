# Multi-Agent Planner

A simple AutoGen project demonstrating how multiple AI agents collaborate to solve a shared task.

Instead of one AI handling everything, three specialized agents work together to create a coordinated plan. This project uses a **family morning planning scenario** to introduce the fundamentals of multi-agent systems in an easy-to-understand way.

---

## Objective

A father has three responsibilities before leaving for work:

- Take Kid 1 to School A before **8:00 AM**
- Take Kid 2 to School B before **8:15 AM**
- Reach the office before **9:00 AM**

The goal is to coordinate these tasks efficiently using multiple AI agents.

---

## AutoGen Concepts Covered

- AssistantAgent
- RoundRobinGroupChat
- System Messages
- Agent Collaboration
- Multi-Agent Planning
- Message Passing
- Termination Condition
- Asynchronous Workflow

---

## Project Architecture

```text
                 User
                   │
                   ▼
        RoundRobinGroupChat
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
School Agent   School Agent   Office Agent
      A             B
     │             │             │
     └─────────────┼─────────────┘
                   ▼
          Coordinated Plan
```

---

## Agents

### School Agent 1

**Responsibility**

- Take Kid 1 to School A
- Ensure arrival before 8:00 AM

---

### School Agent 2

**Responsibility**

- Take Kid 2 to School B
- Ensure arrival before 8:15 AM

---

### Office Agent

**Responsibility**

- Read plans from both school agents
- Verify that all tasks can be completed
- Produce the final coordinated schedule
- End the conversation when planning is complete

---

## Workflow

```text
User
   │
   ▼
Task Description
   │
   ▼
RoundRobinGroupChat
   │
   ▼
Agent 1 proposes plan
   │
   ▼
Agent 2 proposes plan
   │
   ▼
Office Agent reviews
   │
   ▼
All Tasks Completed
   │
   ▼
Conversation Terminates
```

---

## Learning Outcomes

After completing this project you will understand:

- How multiple AI agents collaborate
- How to define specialized agent roles
- How RoundRobinGroupChat works
- How agents exchange messages
- How to coordinate a shared objective
- How termination conditions stop the workflow
- How AutoGen can model real-world collaboration

---

## Example Scenario

Instead of solving everything with a single assistant, each agent is assigned a specific responsibility.

```text
Agent 1
↓

Kid 1 → School A

Agent 2
↓

Kid 2 → School B

Agent 3
↓

Father → Office
```

The Office Agent combines all responses into one coordinated plan before ending the workflow.

---

## Future Improvements

- Add Human-in-the-Loop approval
- Integrate Google Maps APIs
- Add traffic simulation
- Introduce tool calling
- Add memory
- Support dynamic task assignment
- Replace Round Robin with SelectorGroupChat
- Integrate MCP tools
- Add RAG for contextual planning

---

## Technologies Used

- Python
- AutoGen
- Streamlit
- Google Gemini (OpenAI-Compatible API)

---

## References

- Microsoft AutoGen Documentation
- AutoGen AgentChat User Guide
- Microsoft AutoGen GitHub Repository

---

## License

This project is part of my **Generative-AI** learning repository and is intended for educational purposes.