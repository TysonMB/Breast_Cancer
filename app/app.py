import streamlit as st
from pathlib import Path
import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict_page import show_app_info_page, show_predict_page, personnal_info, results
from src.contact import show_contact_page
from src.about import show_about_page

pages = st.sidebar.radio("",["Predict", "About", "Contact"], label_visibility= "collapsed")

if pages == "Predict":
    show_app_info_page()
    personnal_info()
    show_predict_page() 
    results()
     
elif pages == "About":
    show_about_page() 

else:
    show_contact_page()
