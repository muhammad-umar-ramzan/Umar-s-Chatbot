import os
import re
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Umar's Bot!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# User details
USER_DETAILS = {
    "name": "Muhammad Umar",
    "education": "Final-year BS Computer Science student",
    "field": "Data Science and Machine Learning",
    "internships": [
        "Machine Learning Engineer Intern at Technocolabs Softwares",
        "Data Science Internship at EVOASTRA VENTURES",
    ],
    "skills": [
        "Python", "Data Analysis", "Deep Learning", "Machine Learning",
        "SQL", "EDA", "Feature Engineering", "Model Training",
    ],
    "projects": [
        "Home Price Prediction using Linear Regression",
        "Employee Attrition Forecast Analysis and Prediction",
        "Skin Cancer Detection Model using Deep Learning",
    ],
    "interests": [
        "Data Science", "Machine Learning", "Deep Learning",
    ],
    "location": "Toba Tek Singh, Pakistan",
    "job_market": "Saudi Arabian Data Science job market",
}


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title(f"🤖 Chat with {USER_DETAILS['name']}'s Bot!")


# Function to handle specific user questions about Umar
def handle_user_query(user_prompt):
    user_prompt_lower = user_prompt.lower()

    # Responses related to Umar
    umar_related_patterns = [
        ("who is umar", f"Umar is my creator."),
        (
        "tell me about umar", f"Umar is my creator, a {USER_DETAILS['education']} focused on {USER_DETAILS['field']}."),
        ("what is umar's background",
         f"Umar is a {USER_DETAILS['education']} with a focus on {USER_DETAILS['field']} and has experience in {', '.join(USER_DETAILS['internships'])}."),
        ("who created you", f"Umar is my owner."),
        ("who is the owner of this bot", f"Umar is my owner."),
        ("what do you know about umar",
         f"Umar is my creator, a {USER_DETAILS['education']} specializing in {USER_DETAILS['field']}. He has worked on various data science projects and has expertise in {', '.join(USER_DETAILS['skills'])}."),
        ("what is umar's job market", f"Umar is targeting the {USER_DETAILS['job_market']}."),
        ("what are umar's skills", f"Umar has skills in {', '.join(USER_DETAILS['skills'])}."),
        ("what are umar's projects", f"Umar has worked on projects such as {', '.join(USER_DETAILS['projects'])}."),
        ("where is umar from", f"Umar is from {USER_DETAILS['location']}."),
        ("tell me more about umar",
         f"Umar is a {USER_DETAILS['education']} with expertise in {USER_DETAILS['field']}. He has interned at {', '.join(USER_DETAILS['internships'])} and worked on projects like {', '.join(USER_DETAILS['projects'])}. Umar's skills include {', '.join(USER_DETAILS['skills'])}, and he is interested in Data Science and Machine Learning. Umar is currently targeting job opportunities in the {USER_DETAILS['job_market']} and is based in {USER_DETAILS['location']}."),
    ]

    # Loop through patterns and return matched response
    for pattern, response in umar_related_patterns:
        if re.search(pattern, user_prompt_lower):
            return response

    return None


# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Umar's Bot...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Handle predefined queries
    predefined_response = handle_user_query(user_prompt)
    if predefined_response:
        # Display the predefined response
        with st.chat_message("assistant"):
            st.markdown(predefined_response)
    else:
        # Send user's message to Gemini-Pro and get the response
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
