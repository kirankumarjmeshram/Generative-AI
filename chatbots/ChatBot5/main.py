import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY missing in .env file")
    st.stop()

# Initialize OpenAI client
client = genai.Client(api_key=api_key)

# Streamlit UI settings
st.set_page_config(page_title="ChatBot 5 - Streaming", page_icon="🌊")
st.title("🌊 ChatBot 5 — Streaming Responses")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox("Model", ["gemini-2.5-flash", "gemini-2.5-pro"], index=0)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    st.divider()
    st.subheader("📊 Stats")
    if "messages" in st.session_state:
        st.metric("Messages", len(st.session_state.messages))
    
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

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
    
    # Generate streaming response
    with st.chat_message("assistant"):
        # Create a placeholder for streaming
        message_placeholder = st.empty()
        full_response = ""
        
        # # Stream response from OpenAI
        # stream = client.chat.completions.create(
        #     model=model,
        #     messages=st.session_state.messages,
        #     temperature=temperature,
        #     stream=True  # Enable streaming
        # )
        
        # # Collect and display chunks as they arrive
        # for chunk in stream:
        #     if chunk.choices[0].delta.content is not None:
        #         full_response += chunk.choices[0].delta.content
        #         message_placeholder.markdown(full_response + "▌")  # Cursor effect
        
        # for gemini sdk st.session_state.messages looks like
        prompt = ""

        for msg in st.session_state.messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            prompt += f"{role}: {msg['content']}\n"
        
        # here generate_content_stream() → automatically streams the response. 
        stream = client.models.generate_content_stream(
                model=model,
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=temperature
                )
        )

        for chunk in stream:
            if chunk.text:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌") #cursor effect
                # Final update without cursor
        
        message_placeholder.markdown(full_response) # final update without cursor
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer info
st.sidebar.divider()
st.sidebar.info("""
**✨ Features:**
- Real-time streaming responses
- Cursor effect while typing
- Adjustable model & temperature
- Full conversation history
""")