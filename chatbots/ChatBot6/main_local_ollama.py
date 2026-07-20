import streamlit as st
import ollama

st.set_page_config(
    page_title="ChatBot 6 - Local LLM",
    page_icon="🤖"
)

st.title("🤖 ChatBot 6 — Local LLM (DeepSeek-R1)")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.7
    )

    st.divider()

    st.info("""
**Local LLM**

- Model: DeepSeek-R1:1.5B
- Runs completely on your computer
- No API Key required
- No internet required (after installation)
""")

    st.divider()

    if "messages" in st.session_state:
        st.metric("Messages", len(st.session_state.messages))

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()


MODEL = "deepseek-r1:1.5b"

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat Input
if prompt := st.chat_input("Type your message..."):

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ollama.chat(
                model=MODEL,
                messages=st.session_state.messages,
                options={
                    "temperature": temperature
                }
            )

            assistant_reply = response["message"]["content"]

            st.write(assistant_reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )