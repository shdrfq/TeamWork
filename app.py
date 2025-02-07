import streamlit as st
import google.generativeai as genai

# Set Gemini API Key
genai.configure(api_key="AIzaSyCnRo7z_mSe-518MqQcp18qV0QaXeTmsIE")

# Function to generate response
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("🤖 Chatbot with ISSA Tech Solution")
st.write("Powered by ISSA Tech Solution")

# User input
user_input = st.text_input("You: ", "")


if user_input:
    response = get_gemini_response(user_input)
    st.text_area("Bot:", value=response, height=200, disabled=True)
