# ChatBot3 : Advance Chatbot (Model + Temperature Control)

* **LangChain "Chat Model" Integration:** Instead of the native OpenAl client (used in Chatbot 2),
  this bot uses LangChain's ChatOpenAl wrapper. This prepares the application for easier switching between different LLM providers in the future if needed.
* **Manual Message "Translation":** The code manually converts Streamlit's simple dictionary
  history (role/content) into LangChain's specific schema objects (HumanMessage and AlMessage) before sending them to the model.
* **Full Context Injection:** It does not use a dedicated "Memory" class yet. Instead, it passes the entire list of converted messages to Ilm.invoke() on every turn, forcing the model to read the whole conversation history to generate the next answer.
* **Dynamic User Controls:** It introduces a Sidebar (st.sidebar), allowing the user to dynamically change the Model (gpt-40 vs mini) and Temperature (creativity) without restarting the code.
* **Chat Management:** It includes a "Clear Chat" button that resets st.session_state, demonstrating how to programmatically wipe session memory.

## How this Chatbot Works

User Message
      │
      ▼
Session State History
      │
      ▼
ChatOpenAI / Gemini Model
      │
      ▼
Assistant Response

## Improvements

* Model Selector
* Temperature Slider
* Clear chat button
* Side bar settings panel

## Limitations

* Still manual memory
* No long-term memory
* No persistent memory
* No tools / retrival / DB
* Still not suitable for productio
