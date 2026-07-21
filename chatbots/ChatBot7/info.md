# ChatBot 7 : Modern LangChain Chatbot (RunnableWithMessageHistory)

A modern AI chatbot built with **Streamlit**, **LangChain**, and **Google Gemini** using **RunnableWithMessageHistory** for managing conversation history. This chatbot demonstrates the latest LangChain architecture with LCEL (LangChain Expression Language).

---

## Features

- ✨ Modern LangChain Architecture
- 🤖 Google Gemini Integration
- 🧠 RunnableWithMessageHistory
- 📝 ChatPromptTemplate
- 💬 Session-based Conversation Memory
- 🌡️ Adjustable Temperature
- 🔄 Dynamic Gemini Model Selection
- 📋 View Raw Message History
- 🧹 Clear Chat Functionality

---

## Prerequisites

- Python 3.10+
- Google Gemini API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Install Dependencies

```bash
pip install streamlit python-dotenv langchain langchain-google-genai langchain-community
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
ChatBot-7/
│── app.py
│── .env
│── README.md
```

---

## How it Works

```text
        User Message
              │
              ▼
    ChatPromptTemplate
              │
              ▼
RunnableWithMessageHistory
              │
              ▼
 ChatGoogleGenerativeAI
              │
              ▼
 Assistant Response
              │
              ▼
 Update ChatMessageHistory
```

---

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini
- RunnableWithMessageHistory
- ChatPromptTemplate

---

## Limitations

- Requires a Google Gemini API Key
- Conversation history is stored only during the current Streamlit session
- No streaming responses
- No vector database or RAG
- No tool/function calling
- No persistent database storage

```

```
