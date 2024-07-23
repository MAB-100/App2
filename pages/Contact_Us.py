import streamlit as st

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input(label="Enter your email")
    user_message = st.text_area(label="Enter your message")
    button = st.form_submit_button(label="Send")

    if button:
        st.write("Email sent successfully")
        st.write("Thank you for contacting us")
