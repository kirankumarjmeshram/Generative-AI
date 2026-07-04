import streamlit as st
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY missing in .env file")
    st.stop()

# Streamlit UI settings
st.set_page_config(page_title="ChatBot 3 - LangChain Session Chat", page_icon="🤖")
st.title("🤖 ChatBot 3 — LangChain + Session Chat History")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox("Model", ["gemini-2.5-flash", "gemini-2.5-pro"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.5)

    if st.button("🧹 Clear Chat"):
        st.session_state["messages"] = []
        st.rerun()

# Initialize session chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle user input
if user_input := st.chat_input("Type your message..."):
    # Append user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Build messages list for LangChain
    lc_messages = []
    for m in st.session_state["messages"]:
        if m["role"] == "user":
            lc_messages.append(HumanMessage(content=m["content"]))
        else:
            lc_messages.append(AIMessage(content=m["content"]))

    # Initialize LLM
    llm = ChatGoogleGenerativeAI(google_api_key=api_key, model=model, temperature=temperature)

    # Invoke LLM using message history
    response = llm.invoke(lc_messages)
    bot_reply = response.content

    # Save bot response
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)
