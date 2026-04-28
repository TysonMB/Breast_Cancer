import streamlit as st


def show_contact_page():
    
    name = st.text_input(placeholder = "Enter your name", label = "")
    st.write("")
    email = st.text_input(placeholder = "Enter your eamil", label = "")
    st.write("")
    area_text = st.text_area(placeholder = "Write you message here.", label = "")
    st.write("")
    submit_button = st.button(label = "Submit")

    if submit_button:
        if not name:
            st.warning("Please fill in your name.")
        elif not email:
            st.warning("Please enter email address")
        elif not area_text:
            st.warning("Please typing your meassage.")
        else:
            st.success("Your message was sent")