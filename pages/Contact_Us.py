import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input(label="Enter your email")
    user_message = st.text_area(label="Enter your message")
    button = st.form_submit_button(label="Send")

    if button:
        send_email(user_email, user_message)
        st.info("Email sent successfully")
