import os
import streamlit as st 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
gemini_api_key = os.environ.get("GEMINI_API_KEY")

st.set_page_config(page_title = "ChatBot 1 - Hello LLM", page_icon="🤖")
st.title("🤖 Chatbot 1 - Hello LLM (Stateless)")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             temperature=0.3,
                             api_key = gemini_api_key
                             )

prompt = st.text_input("Ask something")

if prompt:
    response = llm.invoke(prompt)
    st.write("**Answer:**", response.content)

