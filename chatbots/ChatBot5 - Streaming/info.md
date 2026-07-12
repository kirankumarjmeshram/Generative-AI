
# ChatBot 5 : Streaming Chatbot (Real-Time Responses)

## Features

- **Real-Time Streaming:** Uses Gemini's `generate_content_stream()` API to stream the response token-by-token instead of waiting for the complete response, creating a faster and more interactive user experience.
- **Typing Cursor Effect:** Displays a cursor (`▌`) while the model is generating text, simulating a real-time typing experience similar to modern AI chat applications.
- **Conversation Context:** Maintains chat history using `st.session_state`. Since the Gemini SDK does not directly accept Streamlit's message format, the conversation history is converted into a single prompt before being sent to the model.
- **Adjustable Model Selection:** Users can switch between different Gemini models (`gemini-2.5-flash` and `gemini-2.5-pro`) from the sidebar.
- **Temperature Control:** Allows users to dynamically adjust the model's creativity using a temperature slider.
- **Session-Based Chat History:** Stores all user and assistant messages in `st.session_state`, preserving the conversation throughout the current Streamlit session.
- **Chat Statistics:** Displays the total number of messages exchanged in the current conversation.
- **Clear Chat:** Resets the conversation history with a single button.

---

## How this Chatbot Works

```text
        User Message
              │
              ▼
     Session State History
              │
              ▼
 Convert History to Prompt
              │
              ▼
 Gemini Streaming API
(generate_content_stream)
              │
              ▼
 Stream Response Chunks
              │
              ▼
 Update UI in Real Time
              │
              ▼
    Assistant Response
```

---

## Improvements

- Real-Time Streaming Responses
- Token-by-Token Text Generation
- Typing Cursor Animation
- Conversation Context Support
- Model Selector
- Temperature Control
- Session-Based Chat History
- Chat Statistics Panel
- Clear Chat Button
- Better User Experience (UX)

---

## Limitations

- Chat history is manually converted into a prompt string
- No LangChain Integration
- No Conversation Memory abstraction
- Context grows with longer conversations
- No persistent memory after application restart
- No vector database or RAG
- No tool/function calling
- Not suitable for production-scale applications
