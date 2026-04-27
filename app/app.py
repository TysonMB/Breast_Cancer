import streamlit as st
from pathlib import Path
import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from pages.predict_page import show_app_info_page, show_predict_page, personnal_info, results
from pages.contact_page import show_contact_page
from pages.about_page import show_about_page

  

predict = st.Page(
    "pages/predict_page.py",
    title="Predict",
    icon="🏠" 
)

about = st.Page(
    "pages/about_page.py",
    title="About",
    icon="🧠"
)

contact = st.Page(
    "pages/contact_page.py",
    title="Contact",
    icon="📊"
) 

page = st.navigation([predict, about, contact])

page.run()

if page == predict:
    show_app_info_page()
    personnal_info()
    show_predict_page() 
    results() 
    
elif page == about:
    show_about_page() 

else:
    show_contact_page()