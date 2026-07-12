
# ChatBot 5 : Summary Memory Chatbot (ConversationSummaryMemory)

## Features

- **Conversation Summary Memory:** Uses LangChain's `ConversationSummaryMemory` to automatically summarize older conversations instead of storing the entire chat history. This helps maintain context while reducing the number of tokens sent to the LLM.
- **Automatic Memory Management:** The memory class continuously updates the conversation summary after each interaction, eliminating the need for manual chat history management.
- **ConversationChain Integration:** Uses LangChain's `ConversationChain`, which combines the LLM and summary memory into a single chain. Calling `predict(input=user_input)` automatically injects the conversation summary into the prompt.
- **Efficient Context Handling:** Instead of sending every previous message, the chatbot sends a summarized history along with recent conversation, making it suitable for longer chats.
- **Conversation Summary Viewer:** Displays the generated conversation summary in an expandable section, allowing users to see exactly what the AI remembers.
- **Memory Buffer Inspection:** Provides a sidebar expander to inspect the current memory variables for debugging and learning purposes.
- **Dynamic Model & Temperature:** Allows users to switch between Gemini models and adjust the temperature directly from the sidebar.
- **Clear Chat History:** Clears both the displayed conversation and the summary memory, starting a fresh chat session.

---

## How this Chatbot Works

```text
                 User Message
                       │
                       ▼
              ConversationChain
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
 Load Summary   Build Final Prompt   Call Gemini
       │               │                │
       └───────────────┼────────────────┘
                       │
                       ▼
      ConversationSummaryMemory
       (Old Chats → Summary)
                       │
                       ▼
         ChatGoogleGenerativeAI
                       │
                       ▼
         Generate AI Response
                       │
                       ▼
 ConversationChain Updates Summary
                       │
                       ▼
          Assistant Response
```

---

## Improvements

- Conversation Summary Memory
- Automatic Context Summarization
- Efficient Token Usage
- Better Long Conversation Support
- ConversationChain
- Automatic Memory Management
- Memory Summary Viewer
- Memory Buffer Inspector
- Dynamic Model Selection
- Temperature Control
- Clear Chat Button

---

## Limitations

- Summary quality depends on the LLM
- Fine details from older conversations may be lost after summarization
- No persistent memory after application restart
- No vector database or RAG
- No tool/function calling
- No streaming responses
- Not suitable for production-scale applications
