import streamlit as st

st.set_page_config(page_title="Streamlit UI vs Chatbot", layout="centered")

# -----------------------------
# 1️⃣ Title Example
# -----------------------------
st.title("🤖 My LangChain ChatBot")

# -----------------------------
# 2️⃣ Subheader Example
# -----------------------------
st.subheader("Talk to your assistant below 👇")

# -----------------------------
# 3️⃣ Text Input Example
# -----------------------------
st.text_input("You:", placeholder="Type here...", key="txt_input_demo")

# -----------------------------
# 4️⃣ Button Example
# -----------------------------
st.button("Send", key="btn_demo")

# -----------------------------
# 5️⃣ Chat Bubble: User Message
# -----------------------------
st.markdown("🧑‍💻 **You:** Hello")

# -----------------------------
# 6️⃣ Chat Bubble: Bot Message
# -----------------------------
st.success("🤖 **Bot:** Hi, how can I help you?")

# -----------------------------
# 7️⃣ Spinner Example
# -----------------------------
import time
with st.spinner("Bot is typing..."):
    time.sleep(2)
    st.success("✅ Done!")

# -----------------------------
# 8️⃣ Expander Example
# -----------------------------
with st.expander("📜 See Full Conversation"):
    st.write("🧑‍💻 You: Hello")
    st.write("🤖 Bot: Hi there!")

# -----------------------------
# 9️⃣ Sidebar Example
# -----------------------------
st.sidebar.title("📌 Chat Settings")
st.sidebar.info("This is where you can explain settings or instructions.")

# -----------------------------
# 🔟 Clear Chat Button
# -----------------------------
st.button("🗑️ Clear Chat", key="clear_btn_demo")

# st.markdown("---")
# st.caption("👉 Uncomment each block to see Streamlit component in action.")
