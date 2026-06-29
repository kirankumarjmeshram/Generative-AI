import streamlit as st
from datetime import datetime

# ------------------------------------------------------------
# Page Setup
# ------------------------------------------------------------
st.set_page_config(page_title="Advanced Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Advanced Chatbot Interface")
st.caption("Powered by Streamlit — Upgrade from Basics → Professional UI")


# ------------------------------------------------------------
# Chat History Using Session State
# ------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ------------------------------------------------------------
# Sidebar (Settings Area)
# ------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Chat Settings")
    temperature = st.slider("Model Temperature", 0.0, 1.0, 0.3)
    st.markdown("---")

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.experimental_rerun()


# ------------------------------------------------------------
# Display Chat Messages in Chat Bubble Format
# ------------------------------------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="🧑‍💻"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg["content"])


# ------------------------------------------------------------
# Chat Input Section
# ------------------------------------------------------------
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display immediately
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    # Simulated bot typing
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = f"You said: {user_input}\n\n(This is a dummy response, integrate LLM here.)"
            st.write(response)

    # Add bot message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
