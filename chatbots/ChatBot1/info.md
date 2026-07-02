# **Chatbot 1 : Simple Stateless Chatbot**

* **Stateless Architecture:** This bot has no memory. Every interaction is treated as a completely new request; it does not remember previous questions or answers.
* **Direct LLM invocation:** It uses the basic llm.invoke(prompt) method from LangChain. The input is sent directly to the model as a single string.
* **Simple Ul Input:** Unlike the later versions, this uses st.text_input (standard text box) rather than the chat-specific st.chat_input.
* **Model Configuration:** It utilizes gpt-40-mini with a low temperature (0.3), making the responses more deterministic and focused.

## How This Stateless Chatbot Works

    **[User Message]**

 **
    |**

 **
    v**

 **[HumanMessage()]**

 **
    |**

 **
    v**

 **[LLM (Chat  Gemini/Open AI)]**

 **
    |**

 **
    v**

 **[Assistant Response]**


## Limitations:

* No memory
* No conversation
* No system prompt
* Not suitable for real chatbots
