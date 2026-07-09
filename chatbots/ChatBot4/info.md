# ChatBot 4 : Memory Chatbot (ConversationBufferMemory)

## Features

- **Automatic Memory Management:** Unlike ChatBot 3, which manually managed the conversation history, this chatbot uses LangChain's `ConversationBufferMemory` to automatically store and maintain the chat history.
- **ConversationChain Integration:** Uses LangChain's `ConversationChain`, which combines the LLM, prompt template, and memory into a single chain. Calling `predict(input=user_input)` automatically injects the conversation history into the prompt.
- **Custom Prompt Template:** Uses a `PromptTemplate` to define the assistant's behavior and format the conversation using `{history}` and `{input}` placeholders.
- **Persistent Memory:** The memory object is stored inside `st.session_state`, allowing the chatbot to remember previous interactions across Streamlit reruns.
- **Memory Buffer Inspection:** Displays the current memory buffer in the sidebar, making it easy to understand what the LLM is remembering during the conversation.
- **Clear Chat History:** Allows users to reset both the displayed conversation and the underlying memory buffer with a single button.

---

## How this Chatbot Works

```text
        User Message
              │
              ▼
     ConversationChain
              │
              ▼
ConversationBufferMemory
 (Automatic Context)
              │
              ▼
 ChatGoogleGenerativeAI
              │
              ▼
    Assistant Response
              │
              ▼
 Memory Automatically Updated
```

---

## Improvements

- Automatic Memory Management
- ConversationBufferMemory
- ConversationChain
- Custom Prompt Template
- Automatic Context Injection
- Persistent Session Memory
- Memory Buffer Viewer
- Cleaner and Simpler Code

---

## Limitations

- Uses only `ConversationBufferMemory`
- Memory grows with longer conversations
- No memory summarization
- No persistent storage after application restart
- No vector database or RAG
- No tool/function calling
- No streaming responses
- Not suitable for production-scale applications
