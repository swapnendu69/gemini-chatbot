from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

st.title("Your Next-Gen Personal Chatbot", anchor=False)
st.divider()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

question = st.text_input("Ask me", placeholder="Type your query")

if st.button("Ask Gemini", type="primary"):
    if not question.strip():
        st.warning("Please type your query first!")
    else:
        with st.spinner("Thinking..."):
            interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=question,
            )
        st.markdown(interaction.output_text)
