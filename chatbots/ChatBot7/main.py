import streamlit as st
from dotenv import load_dotenv
import os

# Modern LangChain imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY missing in .env file")
    st.stop()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Modern Gemini Chatbot", page_icon="✨")
st.title("✨ Modern Gemini Chatbot — RunnableWithMessageHistory")

with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "Gemini Model",
        ["gemini-1.5-flash", "gemini-1.5-pro"],
        index=0
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.store = {}
        st.rerun()

# -----------------------------
# Initialize Store (memory for sessions)
# -----------------------------
if "store" not in st.session_state:
    st.session_state.store = {}

def get_history(session_id: str):
    """Returns the chat history object for the session."""
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]


# -----------------------------
# Initialize LLM (Modern API)
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model=model,
    api_key=api_key,
    temperature=temperature
)

# -----------------------------
# Prompt Template (Modern API)
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("placeholder", "{history}"),
    ("human", "{input}")
])


# -----------------------------
# Create the Conversation Chain (Modern Way)
# -----------------------------
# prompt → llm
chain = prompt | llm

# Add memory wrapper
chain_with_memory = RunnableWithMessageHistory(
    chain,                         # the main chain
    get_history,                   # memory store function
    input_messages_key="input",    # the field to pass user input
    history_messages_key="history" # internally used key
)

# -----------------------------
# Initialize message list for display
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# Handle Chat Input
# -----------------------------
if user_input := st.chat_input("Ask Gemini..."):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Invoke chain with memory
    response = chain_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "gemini_chat"}}
    )

    assistant_message = response.content

    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    with st.chat_message("assistant"):
        st.write(assistant_message)


# -----------------------------
# Sidebar: Show memory store
# -----------------------------
with st.sidebar:
    st.subheader("🧠 Raw Memory (Message History)")
    history = get_history("gemini_chat")
    st.json(history.messages)
