# Chatbot 4-Memory Chatbot (Automated Context)

* **Automated Memory Management:** This is the first bot to use LangChain's dedicated
  ConversationBufferMemory class. It automatically stores and manages the history, removing the need to manually "translate" or append messages to a list before every API call.
* **ConversationChain:** It utilizes the ConversationChain object. This wrapper combines the LLM and the Memory into a single entity. You simply call.predict(input=prompt), and the chain handles the context injection automatically.
* **Persistent Chain State:** The code stores the entire chain object in
  st.session_state.conversation. This ensures that the memory buffer inside the chain persists across Streamlit's re-runs (every time the user clicks or types).
* **Memory Inspection:** It features an "Expander" (st.expander) that allows the user to view the raw memory.buffer. This is excellent for debugging or teaching purposes, as it shows exactly what "text" the Al is remembering.
* **Robust Error Handling:** It wraps the prediction logic in a try-except block, ensuring the app doesn't crash if the API call fails (e.g., network issues or quota limits).
