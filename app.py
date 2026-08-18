"""
FAQ Chatbot - Streamlit UI
CodeAlpha AI Internship - Task 2
"""

import streamlit as st
from chatbot import FAQChatbot

st.set_page_config(page_title="University FAQ Chatbot", page_icon="🎓")

st.title("🎓 University Admissions FAQ Chatbot")
st.caption("CodeAlpha AI Internship — Task 2 (Demo project, sample data)")

# Load chatbot once and cache it (avoids rebuilding TF-IDF on every message)
@st.cache_resource
def load_chatbot():
    return FAQChatbot()

bot = load_chatbot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I can answer questions about university admissions — fees, deadlines, "
                       "eligibility, scholarships, and more. What would you like to know?",
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input box
user_input = st.chat_input("Ask a question about admissions...")

if user_input:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get chatbot response
    result = bot.get_response(user_input)
    answer = result["answer"]

    # Show assistant's response
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
        if result["matched_question"]:
            st.caption(f"Matched FAQ: \"{result['matched_question']}\" (similarity: {result['score']:.2f})")

# Sidebar with sample questions
with st.sidebar:
    st.subheader("Try asking:")
    st.write("- What is the last date for admission?")
    st.write("- How much is the semester fee?")
    st.write("- Is there a scholarship available?")
    st.write("- What documents are required?")
    st.write("- Does the university have hostel facilities?")

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()
