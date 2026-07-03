import os
import streamlit as st 
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Safety check
if not api_key:
    st.error("API key not found! Please add GEMINI_API_KEY to your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

st.set_page_config(page_title = "ChatBot 2 - Basic Chat", page_icon="💬")
st.title("💬 ChatBot 2 — Basic Streamlit + Gemini Chatbot")

# Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display privious messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# chat input
if user_input := st.chat_input("Ask something..."):
    # Add user message
    st.session_state["messages"].append(
        {
        "role": "user",
        "content": user_input
        }
    )
    with st.chat_message("user"):
        st.write(user_input)

# convert chat history into prompt
prompt = ""
for msg in st.session_state["messages"]:
    role = "User" if msg["role"] == "user" else "Assistant"
    prompt += f"{role}: {msg['content']}\n"

# Generate Gemini response
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)

bot_replay = response.text

# Add bot message
st.session_state["messages"].append(
    {
        "role":"assistant", 
        "content":bot_replay
     }
)

with st.chat_message("assistant"):
    st.write(bot_replay)