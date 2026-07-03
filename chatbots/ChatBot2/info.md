# Chatbot 2: Session Memory Chatbot (Manual Memory)

* **Native OpenAl Client:** Unlike the other bots in this list, this one uses the native google library directly, rather than LangChain. This shows how to build a bot without any wrapper frameworks.
* **Manual Session History:** It implements memory by manually appending user and assistant messages to a list in st.session_state("messages"].
* **Context Awareness:** To make the bot "remember" the conversation, it passes the entire list of past messages (st.session_state("messages"]) to the OpenAl API every time a new prompt is sent.
* **Modern Chat UI:** It utilizes Streamlit's native chat elements-st.chat_input (for the bottom text bar) and st.chat_message (for user/bot bubbles)-providing a familiar messaging interface compared to the simple text box in Chatbot 1.
* **Improved Security:** It loads the API key from a .env file using python-dotenv, which is a best practice compared to hardcoding it.

## How This Chatbot Works

**[User Message]
              |
              v
 [Store in session_state]
              |
              v
 [Convert to LangChain Messages]
              |
              v
 [LLM (Chat Gemini/Open AI)]
              |
              v
 [Append to session_state]**

## Improvements

* Remember previous user messages
* Conversations feel  natural
* Maintains basic context
* Works for simple support/chat apps

## Limitations

* Memory is mannually built
* No real langchain memory
* Code become messy
* Not scalable
