import streamlit as st
import google.generativeai as genai

# Configure API Key securely from Streamlit secrets (recommended for Streamlit Cloud)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize Gemini model (correct model name for Gemini 1.5 Flash)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("🧠 AI Code Reviewer")
st.write("Submit your Python code for review and get bug reports & fixes!")

# User Input
code_input = st.text_area("Paste your Python code here:", height=200)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Reviewing your code... ⏳"):
            user_prompt = f"""
            You are a professional Python code reviewer.
            - Analyze the following Python code for **errors, inefficiencies, and improvements**.
            - Provide a **bug report** with explanations.
            - Give a **fully corrected version** of the code.

            Here is the user's code:
            ```python
            {code_input}
            ```

            Please return the response in **Markdown format**, with these sections:
            1. **Bug Report** - List errors with explanations.
            2. **Fixed Code** - Corrected Python code inside a code block.
            """

            try:
                # Generate response (corrected format - wrap in list)
                response = model.generate_content([user_prompt])

                # Show AI review report
                st.subheader("🔍 AI Code Review Report")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"🚨 Error generating response: {e}")

    else:
        st.warning("⚠️ Please enter Python code before submitting.")
