import streamlit as st
from google import genai

st.set_page_config(page_title="StudyMate AI", page_icon="🤖")

st.title("🤖 StudyMate AI")
st.write("Your personal AI study assistant")

api_key = st.text_input("Enter Gemini API Key", type="password")

question = st.text_area(
    "Ask your question:",
    placeholder="Example: Explain Python loops in simple words"
)

if st.button("Ask AI"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""
            You are StudyMate, a helpful college study assistant.

            Explain concepts in simple language.
            Give examples when useful.
            Keep answers suitable for students.

            Student question:
            {question}
            """
        )

        st.subheader("🤖 StudyMate")
        st.write(response.text)
