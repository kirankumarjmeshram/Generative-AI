import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Chatbot Demo", layout="centered")

st.title("🤖 My First Chatbot")
st.subheader("Talk to your assistant below 👇")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", placeholder="Type your message here...")

# When user clicks Send
if st.button("Send") and user_input:
    # Append user message and dummy bot reply
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", "This is a sample response."))  # You can add actual response later

# Show chat history like a conversation
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"🧑‍💻 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")

# Optional: Expandable section to view all messages
with st.expander("📜 Full Chat Log"):
    for sender, message in st.session_state.chat_history:
        st.write(f"{sender}: {message}")
