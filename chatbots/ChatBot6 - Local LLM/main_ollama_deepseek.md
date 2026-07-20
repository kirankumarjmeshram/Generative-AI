# ChatBot 6 : Local LLM Chatbot (DeepSeek-R1)

A simple AI chatbot built with **Streamlit** and **Ollama** that runs the **DeepSeek-R1:1.5B** language model locally. Unlike cloud-based chatbots, this application does not require an API key and works offline after the model is installed.

---

## Features

- 🖥️ Runs a local LLM using Ollama
- 🤖 Uses DeepSeek-R1:1.5B model
- 💬 Interactive Streamlit chat interface
- 🌡️ Adjustable temperature
- 💾 Session-based chat history
- 📊 Message counter
- 🧹 Clear chat functionality
- 🔑 No API key required

---

## Prerequisites

- Python 3.10+
- Ollama installed
- DeepSeek-R1:1.5B model downloaded

Download the model:

```bash
ollama pull deepseek-r1:1.5b
```

---

## Install Dependencies

```bash
pip install streamlit ollama
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Project Structure

```
ChatBot-6/
│── app.py
│── README.md
```

---

## How it Works

```text
        User Message
              │
              ▼
     Streamlit Chat UI
              │
              ▼
      Session State Memory
              │
              ▼
        Ollama Chat API
              │
              ▼
      DeepSeek-R1:1.5B
        (Local LLM)
              │
              ▼
     Assistant Response
```

---

## Technologies Used

- Python
- Streamlit
- Ollama
- DeepSeek-R1:1.5B

---

## Limitations

- Requires Ollama to be installed
- Requires the DeepSeek model to be downloaded
- Conversation history is stored only for the current session
- No streaming responses
- No long-term memory

```

```
