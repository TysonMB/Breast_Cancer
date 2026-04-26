import streamlit as st


def show_about_page():
    st.title("About App")
    st.divider()

    st.write("""### Brief description of the app""")
    st.write("")
    st.write("""
    This app was developed using the Breast Cancer dataset from keggle. The dataset has 31 features including the target set.
    After performing muiltiple test using different models and using different paramaters, the most important features to predict
    were the three used in this app.

    The form needs to be filled, if there is any missing field in the form will not work. However ths other fields like first name,
    last name, age and marital status can be left out.
    
    """)

