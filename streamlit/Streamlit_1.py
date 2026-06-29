import streamlit as st

# -------------------------------
# 1️⃣ Page Title
# -------------------------------
st.set_page_config(page_title="Chatbot Interface", layout="centered")
st.title("🤖 Chatbot Interface")

# -------------------------------
# 2️⃣ Subheading / Description
# -------------------------------
st.subheader("Talk to your assistant below 👇")

# -------------------------------
# 3️⃣ Text Input (User Message)
# -------------------------------
user_message = st.text_input("You:", key="user_input")

# -------------------------------
# 4️⃣ Submit Button
# -------------------------------
if st.button("Send"):
    if user_message.strip() != "":
        st.success("🤖 Bot: (Response will come here...)")
        st.info(f"🧑‍💻 You: {user_message}")
    else:
        st.warning("Please type a message before sending.")

# -------------------------------
# 5️⃣ Chat History Expander (Optional)
# -------------------------------
with st.expander("📜 Show Chat History"):
    st.write("Chat history will be shown here...")
