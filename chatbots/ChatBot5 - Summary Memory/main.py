import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.memory import ConversationSummaryMemory
from langchain_classic.chains import ConversationChain
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY missing in .env file")
    st.stop()

# Streamlit UI settings
st.set_page_config(page_title="ChatBot 5 - Summary Memory", page_icon="🧠")
st.title("🧠 ChatBot 5 — Conversation Summary Memory")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "Model", 
        ["gemini-2.5-flash", "gemini-2.5-pro"], 
        index=0)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    st.divider()
    st.subheader("🧠 Memory Type")
    st.info("""
    **ConversationSummaryMemory**
    
    Instead of storing ALL messages (which can exceed token limits), 
    this memory:
    - 📝 Summarizes older conversation
    - 💾 Keeps recent messages in full
    - 🎯 Maintains context efficiently
    - 💰 Saves tokens & costs
    """)
    
    st.divider()
    st.subheader("📊 Stats")
    if "messages" in st.session_state:
        st.metric("Messages", len(st.session_state.messages))
    
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.memory = None
        st.rerun()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model=model,
    temperature=temperature
)

# Create ConversationSummaryMemory if it doesn't exist.
# It automatically summarizes older conversations to reduce token usage.
if "memory" not in st.session_state or st.session_state.memory is None:
    st.session_state.memory = ConversationSummaryMemory(
        llm=llm,
        return_messages=True
    )

# Create a ConversationChain that combines the LLM and summary memory.
# It automatically injects the conversation summary into every request.
conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=True  # Shows what's happening in console
)

# Initialize message history for display
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show current conversation summary at the top
if st.session_state.memory and len(st.session_state.messages) > 4:
    with st.expander("📋 Conversation Summary (What AI Remembers)", expanded=False):
        memory_vars = st.session_state.memory.load_memory_variables({})
        if "history" in memory_vars:
            st.info(memory_vars["history"])
        else:
            st.write("Building summary...")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if user_input := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate response using conversation chain
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = conversation.predict(input=user_input)
            st.write(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Show memory buffer in expandable section
with st.sidebar:
    st.divider()
    with st.expander("🔍 View Memory Buffer"):
        if st.session_state.memory:
            memory_vars = st.session_state.memory.load_memory_variables({})
            st.json(memory_vars)
        else:
            st.write("No memory yet")

# Footer with explanation
st.sidebar.divider()
st.sidebar.success("""
**✨ How It Works:**

1. **Early Messages**: Stored in full
2. **As Chat Grows**: Old messages → summarized
3. **Summary**: Passed as context to LLM
4. **Recent Messages**: Kept in full detail

This prevents token limit errors in long conversations!
""")