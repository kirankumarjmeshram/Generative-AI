import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI #old way of calling the service

# Load environment variables
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Safety check
if not api_key:
    st.error("API key not found! Please add OPENAI_API_KEY to your .env file.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit page setup
st.set_page_config(page_title="ChatBot 2 - Basic Chat", page_icon="💬")
st.title("💬 ChatBot 2 — Basic Streamlit + OpenAI Chatbot")

# Chat input box
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if user_input := st.chat_input("Ask something..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Generate OpenAI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )

    bot_reply = response.choices[0].message.content

    # Add bot message
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)
