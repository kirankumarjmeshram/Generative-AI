import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_classic.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize session state for memory persistence
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# LLM
llm = ChatGoogleGenerativeAI(
    temperature=0.7,
    google_api_key=api_key,
    model="gemini-2.5-flash"
)

# System prompt
system_template = """
You are an AI assistant inside a Streamlit app.
Keep responses clear, friendly, and maintain context.

Chat history:
{history}

User: {input}
AI:
"""

system_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=system_template
)

# Chain
system_chain = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    prompt=system_prompt,
    verbose=True
)

# UI
st.title("🤖 Chatbot 4 - ConversationBufferMemory")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input (this clears automatically after submission)
if user_input := st.chat_input("Ask me anything:"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = system_chain.predict(input=user_input)
            st.write(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Show memory buffer in sidebar
with st.sidebar:
    st.subheader("🔍 Memory Buffer")
    st.write(st.session_state.memory.buffer)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()